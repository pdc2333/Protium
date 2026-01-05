import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

# 设置 MATLAB 风格
plt.style.use(『default』)
plt.rcParams[『font.family』] = 『serif』
plt.rcParams[『font.serif』] = [『Times New Roman』]
plt.rcParams[『mathtext.fontset』] = 『stix』
plt.rcParams[『font.size』] = 12
plt.rcParams[『axes.linewidth』] = 1.2

# 创建 H-S 网格数据
S = np.linspace(-200, 200, 200)  # 熵 S (J/mol·K)
H = np.linspace(-100, 100, 200)  # 焓 H (kJ/mol)
S_grid, H_grid = np.meshgrid(S, H)

# 对于每个(H,S)点，计算满足 G=0 的温度 T = H/S * 1000
# 注意：当 S=0 时，温度会趋于无穷大，需要处理这种情况
T_grid = np.zeros_like(H_grid)

# 计算温度：T = H/S * 1000 (从 kJ/mol 和 J/mol·K 换算)
for i in range(H_grid.shape[0]):
    for j in range(H_grid.shape[1]):
        if abs(S_grid[i,j]) > 1e-6:  # 避免除以零
            T_grid[i,j] = H_grid[i,j] / S_grid[i,j] * 1000
        else:
            # 当 S 接近 0 时，设置温度为一个很大的值或 NaN
            T_grid[i,j] = np.nan

# 限制温度在合理范围内 (100K 到 500K)
T_grid = np.clip(T_grid, 100, 500)

# 创建图形
fig, ax = plt.subplots(figsize=(12, 8))

# 创建颜色映射 - 使用 MATLAB 风格的 jet 色彩映射表示温度
norm = colors.Normalize(vmin=100, vmax=500)
cmap = cm.jet

# 绘制等高面（填充等高线）- 温度作为颜色
contourf = ax.contourf(S_grid, H_grid, T_grid, 
                       levels=50,  # 更多级别以获得平滑渐变
                       cmap=cmap,
                       norm=norm,
                       alpha=0.8)

# 绘制等高线 - 温度等值线
contour = ax.contour(S_grid, H_grid, T_grid, 
                     levels=np.arange(100, 501, 50),  # 从 100K 到 500K，步长为 50K
                     colors=『black』,
                     linewidths=0.5,
                     alpha=0.7)

# 添加等高线标签
ax.clabel(contour, inline=True, fontsize=8, fmt=『%.0f K』)

# 添加 x=0 和 y=0 坐标轴
ax.axhline(y=0, color=『black』, linewidth=1.5, linestyle=『-』, alpha=0.8)
ax.axvline(x=0, color=『black』, linewidth=1.5, linestyle=『-』, alpha=0.8)

# 添加坐标轴标签
ax.text(210, 0, 『S=0』, fontsize=12, ha=『left』, va=『center』, color=『black』)
ax.text(0, 105, 『H=0』, fontsize=12, ha=『center』, va=『bottom』, color=『black』)

# 设置坐标轴标签（包含单位）
ax.set_xlabel(『Entropy S (J/mol·K)』, fontsize=14, labelpad=10)
ax.set_ylabel(『Enthalpy H (kJ/mol)』, fontsize=14, labelpad=10)

# 设置标题
ax.set_title(『Temperature Contour Plot: T = H/S × 1000 (G = H - ts = 0)』, 
             fontsize=16, pad=20, weight=『bold』)

# 添加网格
ax.grid(True, alpha=0.3, linestyle=『--』)

# 设置坐标轴范围
ax.set_xlim([-200, 200])
ax.set_ylim([-100, 100])

# 设置刻度
ax.set_xticks(np.arange(-200, 201, 50))
ax.set_yticks(np.arange(-100, 101, 25))

# 添加颜色条 - 表示温度 T，单位为 K
cbar = plt.colorbar(contourf, ax=ax, shrink=0.8, aspect=20, pad=0.05)
cbar.set_label(『Temperature T (K)』, fontsize=12)
cbar.ax.tick_params(labelsize=10)

# 添加图例说明
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=『red』, alpha=0.8, label=『High Temperature (>400 K)』),
    Patch(facecolor=『blue』, alpha=0.8, label=『Low Temperature (<200 K)』),
    Patch(facecolor=『white』, edgecolor=『black』, linewidth=1.5, label=『Isotherms』)
]
ax.legend(handles=legend_elements, loc=『upper right』, fontsize=11, framealpha=0.9)

# 美化图形
ax.tick_params(axis=『both』, which=『major』, labelsize=11)
ax.set_aspect(『equal』)

# 调整布局并保存
plt.tight_layout()
plt.savefig(『h_s_temperature_contour.png』, dpi=300, bbox_inches=『tight』, 
            facecolor=『white』, edgecolor=『none』)
plt.savefig(『h_s_temperature_contour.pdf』, bbox_inches=『tight』, 
            facecolor=『white』, edgecolor=『none』)

plt.show()

print(「H-S 面温度等高面图创建成功！」)
print(「图像已保存为: h_s_temperature_contour.png 和 h_s_temperature_contour.pdf」)
print(「\n 物理意义:」)
print(「- 此图表示在吉布斯自由能 G=H-ts=0 的条件下」)
print(「- 每个(H,S)点对应的平衡温度 T = H/S × 1000」)
print(「- 颜色表示温度值：红色高温，蓝色低温」)
print(「- 黑色等高线：等温线」)
print(「\n 坐标轴单位:」)
print(「- 焓 H: kJ/mol」)
print(「- 熵 S: J/mol·K」) 
print(「- 温度 T: K」)
print(「\n 数学关系:」)
print(「- 从 G = H - ts = 0 推导出 T = H/S × 1000」)
print(「- 乘以 1000 是因为 H 的单位是 kJ/mol，S 的单位是 J/mol·K」)
