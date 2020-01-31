## 209 Project

ECE209AS Final Project
Cian Costello, Andrew Chen, Mrunal Patel

### Abstract 

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

.
.
.




### References

1) [Passive infrared motion sensors signal processing for Ambient Assisted Living Applications](https://ieeexplore.ieee.org/abstract/document/6229464)

2) [Et tu Alexa, passive wifi sensing for localization](https://arxiv.org/pdf/1810.10109.pdf)

3) [Surveillance tracking using PIR sensors](https://ieeexplore.ieee.org/abstract/document/4472790)

4) [Tracking motion direction and distance with PIR sensors](https://ieeexplore.ieee.org/abstract/document/5503973)

5) [Simultaneous Indoor Tracking and Activity Recognition Using PIR Sensors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5580159/)

6) [Privacy-Preserved Behavior Analysis and Fall Detection by an Infrared Ceiling Sensor Network](https://www.mdpi.com/1424-8220/12/12/16920)
