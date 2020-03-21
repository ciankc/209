import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import itertools
from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

rooms = ['officeCarp', 'hallwayCarp','livingCarp','kitchenCarp','bedroomCarp','bathroomCarp']

class RoomRF():
    models = {}
    train = {}
    train_labels = {}
    test = {}
    test_labels = {}

    def __init__(self):
        for room in rooms:
            self.models[room], self.train[room], self.test[room], self.train_labels[room], self.test_labels[room] = self.run_train(room)
       
    def evaluate():
        for room in rooms:
            model, train, test, train_labels, test_labels = self.models[room], self.train[room], self.test[room], self.train_labels[room], self.test_labels[room]

            n_nodes = []
            max_depths = []
            # Stats about the trees in random forest
            for ind_tree in model.estimators_:
                n_nodes.append(ind_tree.tree_.node_count)
                max_depths.append(ind_tree.tree_.max_depth)
                
            print(f'Average number of nodes {int(np.mean(n_nodes))}')
            print(f'Average maximum depth {int(np.mean(max_depths))}')

            # # Training predictions (to demonstrate overfitting)
            train_rf_predictions, train_rf_probs = self.run_infer(model, train)
            # # Testing predictions (to determine performance)
            rf_predictions, rf_probs = self.run_infer(model, test)
            # Plot formatting
            plt.style.use('fivethirtyeight')
            plt.rcParams['font.size'] = 18
            evaluate_model(rf_predictions, rf_probs, train_rf_predictions, train_rf_probs)
            plt.savefig('figures/' + room + '-roc_auc_curve.png')
            # Confusion matrix
            cm = confusion_matrix(test_labels, rf_predictions)
            plot_confusion_matrix(cm, classes = ['Poor Health', 'Good Health'],
                                  title = 'Health Confusion Matrix')
            plt.savefig('figures/' + room + '-cm.png')

    def run_infer(self, room, test):
        # print("======================TEST")
        # print(test)
        predictions = self.models[room].predict(test)
        probs = self.models[room].predict_proba(test)[:, 1]
        # print("======================PREDICTIONS")
        # print(predictions)
        # print("======================PROBS")
        # print(probs)
        return predictions, probs
        

    def get_room(self, timestamp, candidates=rooms):
        # TODO: test.at[i, 'timestamp'] =  999999999
        test = pd.DataFrame([timestamp], index=[0], columns=['timestamp'])
        # print(test)

        predictions, probs = self.run_infer(candidates[0], test)
        for room in candidates[1:]:
            pred, prob = self.run_infer(room, test)
            predictions = np.concatenate((predictions, pred))
            probs = np.concatenate((probs, prob))
        # did we predict a 1? build a list of indicies to check
        m, mi = -1, -1
        indicies = []
        for i in range(len(candidates)):
            if predictions[i] == 1:
                indicies.append(i)
        if len(indicies) == 0:
            # use lowest prob
            m, mi = 2, 2
            for i in range(len(candidates)):
                if probs[i] < m:
                    m = probs[i]
                    mi = i
            return predictions[mi], probs[mi], mi 
        else:
            # use highest prob
            m, mi = -1, -1
            for i in indicies:
                if probs[i] > m:
                    m = probs[i]
                    mi = i
            return predictions[mi], probs[mi], mi 

            
    def run_train(self, room):
        RSEED = 50
        # Load in data
        df = pd.read_csv('datasets/'+room+'.csv')
        # Extract the labels
        labels = np.array(df.pop(room))
        # 30% examples in test data
        train, test, train_labels, test_labels = train_test_split(df,
                                                 labels, 
                                                 stratify = labels,
                                                 test_size = 0.1, 
                                                 random_state = RSEED)
        # Imputation of missing values
        train = train.fillna(train.mean())
        test = test.fillna(test.mean())
        # Features for feature importances
        features = list(train.columns)

        # Create the model with 100 trees
        model = RandomForestClassifier(n_estimators=100, 
                                       random_state=RSEED, 
                                       max_features = 'sqrt',
                                       n_jobs=-1, verbose = 1)

        # Fit on training data
        model.fit(train, train_labels)
        return model, train, test, train_labels, test_labels
