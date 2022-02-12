# resonance/pitch.py

# Note/Frequency Conversions

import numpy


class note():
    def __init__(self, frequency, letter, octave):
        note.frequency = frequency
        note.name = letter
        note.octave = octave
#  ------------------------------------------------------------------------
#  Frequency<-->Note conversions
#  ------------------------------------------------------------------------


basenotes = numpy.array([["C",  16.35], ["C#", 17.32], ["D",  18.35], ["D#", 19.45], ["E",  20.6], ["F",  21.83], ["F#", 23.12], ["G",  24.5], ["G#", 25.96], ["A",  27.5], ["Bb", 29.14], ["B",  30.87]])


def octaveshift(freq, octaves):
    "Shift the frequency by the given octave value"
    newfreq = float(freq * (2 ** octaves))
    return newfreq


def notelookup(notename):
    "Looks up a notename and returns the base frequency"
    notenames = list(map(lambda n: n[0], basenotes))
    i = notenames.index(notename)
    return float(basenotes[i][1])


def notetofreq(notename, octave):
    "Takes a notename and octave number, returns the frequency"
    base = notelookup(notename)
    return octaveshift(base, octave)


def closestbase(basefreq):
    "Finds the closest match to a base frequency"
    baselist = list(map(lambda n: float(n[1]), basenotes))
    bases = sorted(baselist, key=lambda n: abs((n - basefreq)))
    return bases[0]


def freqlookup(frequency):
    "Looks up a frequency and returns the notename"
    bases = list(map(lambda n: float(n[1]), basenotes))
    i = bases.index(frequency)
    return basenotes[i][0]


def freqtonote(frequency):
    base = frequency
    octavecount = 0
    while (base > 31):
        base = base / 2
        octavecount += 1
    notename = freqlookup(closestbase(base))
    return notename, octavecount

# ------------------------------------------------------------------------
# Frequency generation
# ------------------------------------------------------------------------


def freqadjust(root, interval):
    return (root * ((2 ** 1/12) ** interval))


def freqincr(root):
    return freqadjust(root, 1)


def freqladder(low, high):
    "Builds a chromatic test-sample within the bounds."
    freq = low
    freqs = []
    while (freq < high):
        freqs.append(freq)
        freq = freqincr(freq)
    return freqs
