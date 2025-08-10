import machine


# index = persentase
volts_level = [
    3.200, 3.250, 3.300, 3.350, 3.400, 3.450,
    3.500, 3.550, 3.600, 3.650, 3.700, 3.703,
    3.706, 3.710, 3.713, 3.716, 3.719, 3.723,
    3.726, 3.729, 3.732, 3.735, 3.739, 3.742,
    3.745, 3.748, 3.752, 3.755, 3.758, 3.761,
    3.765, 3.768, 3.771, 3.774, 3.777, 3.781,
    3.784, 3.787, 3.790, 3.794, 3.797, 3.800,
    3.805, 3.811, 3.816, 3.821, 3.826, 3.832,
    3.837, 3.842, 3.847, 3.853, 3.858, 3.863,
    3.868, 3.874, 3.879, 3.884, 3.889, 3.895,
    3.900, 3.906, 3.911, 3.917, 3.922, 3.928,
    3.933, 3.939, 3.944, 3.950, 3.956, 3.961,
    3.967, 3.972, 3.978, 3.983, 3.989, 3.994,
    4.000, 4.008, 4.015, 4.023, 4.031, 4.038,
    4.046, 4.054, 4.062, 4.069, 4.077, 4.085,
    4.092, 4.100, 4.111, 4.122, 4.133, 4.144,
    4.156, 4.167, 4.178, 4.189, 4.200
]


pin = machine.Pin(34)
adc = machine.ADC(pin)
adc.atten(machine.ADC.ATTN_11DB)  # Mengatur rentang input ADC ke 0-3.3V


# https://www.pangodream.es/esp32-getting-battery-charging-level
def get_voltage():
    return adc.read() * 0.0017


def get_level(volts):
    if volts >= 4.2:
        return 100
    if volts <= 3.2:
        return 0;
    idx = 50
    prev = 0
    while True:
        half = int(abs(idx - prev) / 2)
        prev = idx;
        if volts >= volts_level[idx]:
            idx += half
        else:
            idx -= half
        if prev == idx:
            break;
    return idx;
