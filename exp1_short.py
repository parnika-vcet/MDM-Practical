import matplotlib.pyplot as plt

names = ["ELF/VLF", "LF", "MF", "HF", "VHF", "UHF",
         "SHF", "EHF", "Infrared", "Visible", "UV",
         "X-ray", "Gamma"]

start = [3e3, 3e4, 3e5, 3e6, 3e7, 3e8,
         3e9, 3e10, 3e11, 4e14, 8e14, 3e16, 3e19]

end = [3e4, 3e5, 3e6, 3e7, 3e8, 3e9,
       3e10, 3e11, 4e14, 8e14, 3e16, 3e19, 1e21]

plt.figure(figsize=(14, 4))

for i in range(13):
    plt.barh(0, end[i] - start[i], left=start[i],
             color=plt.cm.rainbow(i / 13), edgecolor="black")
    plt.text((start[i] * end[i]) ** 0.5, 0, names[i],
             ha="center", va="center", rotation=90, fontsize=8)

plt.xscale("log")
plt.xlim(1e3, 1e21)
plt.yticks([])
plt.xlabel("Frequency (Hz)")
plt.title("Electromagnetic Spectrum & Wireless Bands")
plt.show()