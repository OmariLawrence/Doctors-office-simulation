import numpy as np
import matplotlib.pyplot as plt
from math import ceil

class Doctor:
    def __init__(self):
        self.nextAvailable = 0

class Patient:
    def __init__(self, arrival):
        self.arrival = arrival
        self.waitStart = arrival + 2
        self.waitTime = 0
        self.totalTime = 0

def makePatients(num):
    patients = []
    time = 0
    arrive = 0
    for x in range(num):
        patients.append(Patient(time))
        time += ceil(np.random.exponential(20))
    return patients

def simulation(patients, Dr):
    time = 0
    waitTimes = []
    serviceTimes = []
    totalTimes = []
    for x in range(len(patients)):
        if Dr.nextAvailable <= patients[x].waitStart:
            time = patients[x].waitStart
        patients[x].waitTime = time - patients[x].waitStart
        waitTimes.append(patients[x].waitTime)
        st = ceil(np.random.exponential(15))
        serviceTimes.append(st)
        time += st
        patients[x].totalTime = st + patients[x].waitTime
        totalTimes.append(patients[x].totalTime)
        dr.nextAvailable = time
    avgTimeSpent = np.mean(totalTimes)
    maxWaitTime = max(waitTimes)
    avgServiceTime = np.mean(serviceTimes)
    maxServiceTime = max(serviceTimes)
    minServiceTime = min(serviceTimes)
    drutil = (sum(serviceTimes)/time)*100
    print("Average time spent in office: ", avgTimeSpent)
    print("Maximum wait Time: ", maxWaitTime)
    print("Average service time: ", avgServiceTime)
    print("Maximum service time: ", maxServiceTime)
    print("Minimum service time: ", minServiceTime)
    print("Doctor Utilisation: ", drutil,"%")
    return waitTimes

patients = makePatients(1000)
dr = Doctor()
times = simulation(patients, dr)
plt.plot(times)
plt.show()
histogram = plt.hist(times)
histogram = plt.xlabel("Wait Times")
histogram = plt.ylabel("Patients")
plt.show()
