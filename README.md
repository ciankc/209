## Passive Room Sensing using OpenSHS
 
ECE209AS Final Project
Cian Costello, Andrew Chen, Mrunal Patel

### Abstract 

Motion sensors have been used commonly in large buildings. There have been developments for using motion sensors in assisted living situations for the elderly. We present a novel approach to detect sensor locations, behavioral patterns of occupants and other details, such as the number of occupants. Using data from a smart home simulator, we train random forests and create a Markov transition matrix to predict current and next rooms given a time stamp. The applications of this model vary from using it to detect anomalies in the behavior of the elderly and alert caretakers of falls to a more malicious nature where an attacker can learn about the living patterns of the residents.

### Proposal

We will use OpenSHS to simulate a smart home with multiple passive infrared (PIR) sensors. Data collected will be based on an actor or actors that will move throughout the home. Time stamped data from the motion sensors will be used to infer room transitions, predict occupant locations, and recognize human activity patterns. We will experiment with different models to predict the above metrics -- Kalman filters, particle filters, and/or Hidden Markov models.

### Project Timeline

* Week 4 - Project definition and abstract, literature review complete
* Week 5 - OpenSHS setup and data collection
* Week 6 - Use data to infer sensor locations
* Week 7 - Use data to recognize human activity patterns
* Week 8 - Use data to determine number of occupants
* Week 9 - Validate models (Kalman filter, Particle filter, Markov Chain etc)
* Week 10 - Finalize presentation and project report

### Prior Work

A 2020 paper from UCSB [2] uses ambient WiFi signals to detect humans. This is passive sensing, and it does not need any prior knowledge of the WiFi network or devices (including location). Detection rates varied from 86.6-99.9% depending on the number of anchors. Additionally, work has been done to develop new signal processing algorithms for Ambient Assisted Living Applications (AAL) [1]. In this case, time spent in active state by the sensor signal as the best indication of movement intensity. 

---
Background on PIR sensors:

A team from Korea Electronics and Technology Institute [3] used PIR sensors to perform region based human tracking. Six sensors were placed around the ceiling of an office building to track the movement of a single person. Regions were defined by sensor range and overlaps.

More precise information can be derived from PIR sensors, as demonstrated by Zappi et al. [4]. This paper used feature extraction with simple supervised learning algorithms to classify movements of people. This setup involved pairs of PIR sensors facing each other.

A 2017 paper by Luo et al. [5] uses PIR sensors for simultaneous indoor tracking and activity recognition. The paper involves an active setup of groups of sensors on the roof. Each group is arranged in a special way such that the subject can be tracked using bearing and radial segmentation. They use a particle filter to determine the location of the human target. Lastly, they have a two-layer random forest to classify the activity that the human target is performing. They can determine static actions with an accuracy of over 90% (mobile actions were between 60 and 70%).

Another related work on fall detection makes the case for PIR sensors to be used as an alternative to cameras [6]. Since they capture much less detail and information they are inherently more privacy preserving than cameras, not to mention cheaper. They also use roof based sensors, where each sensor is a "pixel" and these pixels are passed to a SVM based classifier and they obtained an average recognition rate of 80%.

---

Similar work has been done on wireless snooping in heavily connected smart homes. Srinivasan et al. [8] presented the Fingerprint and Timing-based Snooping (FATS) attack, which eavesdrops on the wireless transmission of various sensors in a home to classify activities such as cooking, showering, or sleeping. This attack uses wireless fingerprinting and temporal data to cluster sensors by room and make tiered predictions. Various methods to defend against this attack are also presented, including signal attenuation, random delays, and fingerprint masking.

Other related work focused on building room connectivity graphs, which could be applied to the smart energy control of buildings with many rooms. Ellis et al. [9] deployed light and motion sensors into the rooms of a building to determine room connectivity. Predicitons of the next room transition could be used to optimize building energy consumption. The authors created transition matrices for both motion and ambient light sensors to produce their connectivity graphs.

Our work incorporates elements of the previous two ideas in a more constrained scenario, by applying a malicious setting to the goal of learning room connectivity. We assume that an attacker has extracted each room's relevant motion sensor events. Another key difference is the use of a simulated smart home. While less realistic, it allows for more data collection and greater ease in varying the experimental setup. Our results prove the effectiveness of using a simulator like OpenSHS to contribute to applications of malicious passive sensing. 

### Data Collection: OpenSHS
The data collection for our project was done using Open Smart Home Simulator (OpenSHS). This was created in 2017 by Alshammari et al. [7], using the Blender Game Engine and Python to generate 3D simulations of smart homes. The purpose of OpenSHS is to generate large datasets for IoT and machine learning research. We chose to use this platform because it is open source and cross platform, allowing us to develop and test our project on both Mac and Windows machines. Other benefits of OpenSHS include the existing implementation of motion sensors and the interactive usage that allows customized data recording.

Despite clear benefits, we had to make some changes to OpenSHS to fit our project. By default, the smart home in OpenSHS has a wide array of sensors attached to lights, doors, furniture, and appliances. We created an idealized data output with only motion sensor data to more easily use with our predictive models. The motion sensors were implemented as contact sensors in the carpet of each room. More realistic models also exist, such as the "near" or "radar" sensors, which could introduce more uncertainty in measurements and be useful in future work. Additional modifications included adding a column of time stamps to our dataset and inserting a hallway motion sensor to capture data from every room in our sample house.

To process of collecting data works as follows:
1. Run the openshs python script with the "start" option and a context selected.
    ```
    python openshs start -c inside
    ```

2. Set a starting date and time by entering a value at the command line prompt.

3. Start the simulation in blender by pressing the "p" key on your keyboard.

4. Interact with the house, moving avatar with the wasd keys and moving the camera with a mouse. Click to interact with objects when a text prompt appears on the display. This should be done to replicate a daily routine: waking up, going to the bathroom, eating breakfast, etc.

5. Pause the simulation with the spacebar to assign labels to activities and set activity durations (by pressing z and entering a time in seconds).

6. Use the Esc key to end the simulation. The data collected from the simulation will be saved as a csv file with the start time included in the file name.

After a sufficient number of data samples was collected, we were able to use the aggregate feature of OpenSHS to expand our samples into a larger dataset. A replication algorithm is used that randomly draws from our manually collected samples. These samples are sorted based on their activity labeling and aggregated based on the number of activities in each sample. So in order for the aggregate function to be effective, we had to ensure that our manual data was properly labelled. The use of labels helps preserve the logical order of events and create more realistic sensor traces. The aggregate algorithm has options to set the number of days generated, the starting date, the start time variability, and the activity length variability.

### Random Forests

### Markov Chain

### Results and Evaluation

### Limitations

### References

1) [Passive infrared motion sensors signal processing for Ambient Assisted Living Applications](https://ieeexplore.ieee.org/abstract/document/6229464)

2) [Et tu Alexa, passive wifi sensing for localization](https://arxiv.org/pdf/1810.10109.pdf)

3) [Surveillance tracking using PIR sensors](https://ieeexplore.ieee.org/abstract/document/4472790)

4) [Tracking motion direction and distance with PIR sensors](https://ieeexplore.ieee.org/abstract/document/5503973)

5) [Simultaneous Indoor Tracking and Activity Recognition Using PIR Sensors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5580159/)

6) [Privacy-Preserved Behavior Analysis and Fall Detection by an Infrared Ceiling Sensor Network](https://www.mdpi.com/1424-8220/12/12/16920)

7) [OpenSHS: Open Smart Home Simulator](https://www.mdpi.com/1424-8220/17/5/1003/htm)

8) [Protecting your Daily In-Home Activity Information from a Wireless Snooping Attack](https://doi.org/10.1145/1409635.1409663)

9) [Creating a Room Connectivity Graph of a Building from Per-Room Sensor Unit](https://doi.org/10.1145/2422531.2422563)