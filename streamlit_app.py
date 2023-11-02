import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('複素数平面上の x^n = a の解')

# ユーザーから次数nと目標の値aを取得
n = st.slider('次数 (n)', min_value=1, max_value=10, value=2)
a = st.number_input('目標の値 (a)', value=1.0)

# 複素数平面上でx^n=aの解を計算する関数
def calculate_roots(n, a):
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)  # 0から2πまでの角度を均等にn個生成
    roots = np.exp(1j * theta) * np.sqrt(a)  # 指定された次数nと目標の値aに対する解を計算
    return roots

roots = calculate_roots(n, a)  # 指定された次数nと目標の値aに対する解を計算

# 複素数平面上に解をプロット
fig, ax = plt.subplots(figsize=(8, 6))
points = ax.plot(roots.real, roots.imag, 'ro', label=f'x^{n}={a}の解')
ax.set_xlabel('実部')
ax.set_ylabel('虚部')
ax.axhline(y=0, color='k', linewidth=0.5)  # 虚部が0の軸を描画
ax.axvline(x=0, color='k', linewidth=0.5)  # 実部が0の軸を描画
ax.set_title(f'複素数平面上の x^{n}={a} の解')
ax.legend()

# クリックした座標を表示するスポット
spot = ax.plot([], [], 'bo')[0]

st.pyplot(fig)

# 解のテーブルを表示
st.header(f'x^{n}={a}の解')
st.table(list(zip(roots.real, roots.imag)))

st.write(f'注意: 解は複素数平面上に均等に{n}個の点として配置されています。')

# クリックしたときの座標を表示
x, y = st.text_input('座標を入力 (x, y)', '').split(',')
if x and y:
    x, y = float(x), float(y)
    if (x, y) in zip(roots.real, roots.imag):
        spot.set_data(x, y)
        st.write(f'選択した座標: ({x}, {y})')
    else:
        st.write('選択した座標は解の点ではありません。')
