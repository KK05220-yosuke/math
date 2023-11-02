import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('複素数平面上の x^n = 1 の解')

# ユーザーから次数nを取得
n = st.slider('次数 (n)', min_value=1, max_value=10, value=2)

# 複素数平面上でx^n=1の解を計算する関数
def calculate_roots(n):
    theta = np.linspace(0, 2*np.pi, 1000)  # 0から2πまでの角度を生成
    roots = np.exp(1j * theta * n)  # 指定された次数nに対する解を計算
    return roots

roots = calculate_roots(n)  # 指定された次数nに対する解を計算

# 複素数平面上に解をプロット
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(roots.real, roots.imag, label=f'x^{n}=1の解')
ax.set_xlabel('実部')
ax.set_ylabel('虚部')
ax.axhline(y=0, color='k', linewidth=0.5)  # 虚部が0の軸を描画
ax.axvline(x=0, color='k', linewidth=0.5)  # 実部が0の軸を描画
ax.set_title(f'複素数平面上の x^{n}=1 の解')
ax.legend()
st.pyplot(fig)

# 解のテーブルを表示
st.header(f'x^{n}=1の解')
st.table(list(zip(roots.real, roots.imag)))

st.write('注意: 解は複素数平面上に等間隔に配置されています。')
