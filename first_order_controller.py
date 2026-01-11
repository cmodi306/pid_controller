import matplotlib.pyplot as plt
import time

class PID:
    def __init__(self, kp, ki, kd, dt = 0.01):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt

        self.integral = 0
        self.previous_err = 0

    def update(self, setpoint, measurement):
        error = setpoint - measurement # soll_wert - ist_wert
        print("Error: ", error)
        
        # proportional gain
        P = self.kp * error

        # integral
        self.integral += error * self.dt
        I = self.ki * self.integral

        # derivative
        derivative = (error - self.previous_err) / self.dt
        D = self.kd * derivative

        self.previous_err = error

        print("P: ",P)
        print("I: ",I)
        print("D: ",D)

        return P+I+D
    

def main():
    kp=2.6
    ki=2.6
    kd=0.02
    pid = PID(kp=kp, ki=ki, kd=kd, dt = 0.01)
    setpoint = 1.0
    current_measurement = 0.0
    xs, us, ts = [], [], []

    for i in range(2000):
        u = pid.update(setpoint, current_measurement)
        current_measurement += (u-current_measurement) * pid.dt
        print("U:", u)
        print("current_measurement:", current_measurement)
        print()
        xs.append(current_measurement)
        us.append(u)
        ts.append(i)
    
    plt.plot(ts, xs, "b-")
    #plt.plot(us, ts, "r.")
    plt.title(f"PID Response: Kp = {kp}, Ki = {ki}, Kd = {kd}", weight="bold")
    plt.show()

if __name__=="__main__":
    main()