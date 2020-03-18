## 209 Project

ECE209AS Final Project
Cian Costello, Andrew Chen, Mrunal Patel

### Abstract 

Motion sensors have been used commonly in large buildings. There have been developments for using motion sensors in assisted living situations for the elderly. We present a novel approach to detect sensor locations, behavioral patterns of occupants and other details, such as the number of occupants. Using a smart home simulator, we train a model to detect the relevant actions. The applications of this model vary from using it to detect anomalies in the behavior of the elderly and alert caretakers of falls to a more malicious nature where an attacker can learn about the living patterns of the residents.

### Proposal

We will use OpenSHS to simulate a smart home with multiple passive infrared (PIR) sensors. Data collected will be based on an actor or actors that will move throughout the home. Time stamped data from the motion sensors will be used to infer sensor locations, recognize human activity patterns, and determine the number of occupants. We will experiment with different models to predict the above metrics -- Kalman filters, particle filters, and/or Hidden Markov models.

### Project Timeline

* Week 4 - Project definition and abstract, literature review complete
* Week 5 - OpenSHS setup and data collection
* Week 6 - Use data to infer sensor locations
* Week 7 - Use data to recognize human activity patterns
* Week 8 - Use data to determine number of occupants
* Week 9 - Validate models (Kalman filter, Particle filter, Markov Chain etc)
* Week 10 - Finalize presentation and project report

### Prior Work

A 2020 paper from UCSB [2] uses ambient WiFi signals to detect humans. This is passive sensing, and no prior knowledge of the WiFi network or devices (including location) is needed. Detection rates varied from 86.6-99.9% depending on the number of anchors. Additionally, work has been done to develop new signal processing algorithms for Ambient Assisted Living Applications (AAL) [1]. In this case, time spent in active state by the sensor signal as the best indication of movement intensity. 

A team from Korea Electronics and Technology Institute [3] used PIR sensors to perform region based human tracking. Six sensors were placed around the ceiling of an office building to track the movement of a single person. Regions were defined by sensor range and overlaps.

More precise information can be derived from PIR sensors, as demonstrated by Zappi et al. [4]. This paper used feature extraction with simple supervised learning algorithms to classify movements of people. This setup involved pairs of PIR sensors facing each other.

A 2017 paper by Luo et al. [5] uses PIR sensors for simultaneous indoor tracking and activity recognition. The paper involves an active setup of groups of sensors on the roof. Each group is arranged in a special way such that the subject can be tracked using bearing and radial segmentation. They use a particle filter to determine the location of the human target. Lastly, they have a two-layer random forest to classify the activity that the human target is performing. They can determine static actions with an accuracy of over 90% (mobile actions were between 60 and 70%).

Another related work on fall detection makes the case for PIR sensors to be used as an alternative to cameras [6]. Since they capture much less detail and information they are inherently more privacy preserving than cameras, not to mention cheaper. They also use roof based sensors, where each sensor is a "pixel" and these pixels are passed to a SVM based classifier and they obtained an average recognition rate of 80%.


### Data Collection
To gather the data used in this project, we modified the Open Smart Home Simulator (OpenSHS) described in [7], allowing us to quickly simulate PIR sensor data in various room layouts. OpenSHS works as a first person simulation, allowing users to walk through the smarthome and interact with doors, lights, and furniture. As actions are taken, the user can label activities and fast forward time. Our project takes advantage of the motion sensors in each room and the ability to timestamp events. We modified the existing data collection in OpenSHS to only output our target data of the timestamped motion sensor firings. 

### References

1) [Passive infrared motion sensors signal processing for Ambient Assisted Living Applications](https://ieeexplore.ieee.org/abstract/document/6229464)

2) [Et tu Alexa, passive wifi sensing for localization](https://arxiv.org/pdf/1810.10109.pdf)

3) [Surveillance tracking using PIR sensors](https://ieeexplore.ieee.org/abstract/document/4472790)

4) [Tracking motion direction and distance with PIR sensors](https://ieeexplore.ieee.org/abstract/document/5503973)

5) [Simultaneous Indoor Tracking and Activity Recognition Using PIR Sensors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5580159/)

6) [Privacy-Preserved Behavior Analysis and Fall Detection by an Infrared Ceiling Sensor Network](https://www.mdpi.com/1424-8220/12/12/16920)

7) [OpenSHS: Open Smart Home Simulator](https://www.mdpi.com/1424-8220/17/5/1003/htm)