#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os, os.path


#サンプリングレート　librosaデフォルトは22100
sr=44100

#ファイル読み込み
y, sr = librosa.load('/Users/yogurt/nudge-lab/denso/theta-audio-test/thetaV-thetaZ/thetaV/01V.mp3',sr)
print(y.shape, sr)

#短時間フーリエ変換
S = np.abs(librosa.stft(y))

#画像出力
plt.figure(figsize=(10,4))
librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max), sr=sr, y_axis='hz', x_axis='time')
plt.colorbar()
plt.tight_layout()
plt.show()