import numpy as np
import pandas as pd

np.random.seed(42)

n = 500

depth = np.linspace(1000, 3000, n)

wob = np.random.uniform(10, 40, n)
rpm = np.random.uniform(80, 180, n)
flow_rate = np.random.uniform(300, 800, n)
mud_weight = np.random.uniform(9, 14, n)

torque = 0.02 * depth + 0.5 * wob + np.random.normal(0, 5, n)
pressure = 0.03 * flow_rate + 0.5 * mud_weight * 100 + np.random.normal(0, 20, n)

inclination = np.clip(0.01 * depth/10 + np.random.normal(0, 2, n), 0, 90)

rop = (
    0.5 * wob +
    0.3 * rpm -
    0.01 * depth +
    np.random.normal(0, 5, n)
)

df = pd.DataFrame({
    "Depth (m)": depth,
    "WOB (klbs)": wob,
    "RPM": rpm,
    "Flow Rate (gpm)": flow_rate,
    "Mud Weight (ppg)": mud_weight,
    "Torque (kN.m)": torque,
    "Standpipe Pressure (psi)": pressure,
    "Inclination (deg)": inclination,
    "ROP (m/hr)": rop
})

df.to_csv("../data/mwd_data.csv", index=False)

df.head()
