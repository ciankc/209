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
        # TODO: test.at[i, 'Time'] =  999999999
        test = pd.DataFrame([timestamp], index=[0], columns=['Time'])
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

    @staticmethod
    def evaluate_model(predictions, probs, train_predictions, train_probs):
        '''Compare machine learning model to baseline performance.
        Computes statistics and shows ROC curve.'''
        
        baseline = {}
        
        baseline['recall'] = recall_score(test_labels, 
                                         [1 for _ in range(len(test_labels))])
        baseline['precision'] = precision_score(test_labels, 
                                          [1 for _ in range(len(test_labels))])
        baseline['roc'] = 0.5
        
        results = {}
        
        results['recall'] = recall_score(test_labels, predictions)
        results['precision'] = precision_score(test_labels, predictions)
        results['roc'] = roc_auc_score(test_labels, probs)
        
        train_results = {}
        train_results['recall'] = recall_score(train_labels, train_predictions)
        train_results['precision'] = precision_score(train_labels, train_predictions)
        train_results['roc'] = roc_auc_score(train_labels, train_probs)
        
        for metric in ['recall', 'precision', 'roc']:
            print(f'{metric.capitalize()} Baseline: {round(baseline[metric], 2)} Test: {round(results[metric], 2)} Train: {round(train_results[metric], 2)}')
        
        # Calculate false positive rates and true positive rates
        base_fpr, base_tpr, _ = roc_curve(test_labels, [1 for _ in range(len(test_labels))])
        model_fpr, model_tpr, _ = roc_curve(test_labels, probs)

        plt.figure(figsize = (8, 6))
        plt.rcParams['font.size'] = 16
        
        # Plot both curves
        plt.plot(base_fpr, base_tpr, 'b', label = 'baseline')
        plt.plot(model_fpr, model_tpr, 'r', label = 'model')
        plt.legend();
        plt.xlabel('False Positive Rate'); 
        plt.ylabel('True Positive Rate'); plt.title('ROC Curves');
        plt.show();


    @staticmethod
    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Oranges):
        '''
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
        '''
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print('Normalized confusion matrix')
        else:
            print('Confusion matrix, without normalization')

        # print(cm)

        # Plot the confusion matrix
        plt.figure(figsize = (10, 10))
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title, size = 24)
        plt.colorbar(aspect=4)
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45, size = 14)
        plt.yticks(tick_marks, classes, size = 14)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        
        # Labeling the plot
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt), fontsize = 20,
                     horizontalalignment='center',
                     color='white' if cm[i, j] > thresh else 'black')
            
        plt.grid(None)
        plt.tight_layout()
        plt.ylabel('True label', size = 18)
        plt.xlabel('Predicted label', size = 18)
