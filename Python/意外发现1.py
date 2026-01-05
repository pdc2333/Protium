import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置 MATLAB 风格
plt.style.use(『default』)
plt.rcParams[『font.family』] = 『serif』
plt.rcParams[『font.serif』] = [『Times New Roman』]
plt.rcParams[『mathtext.fontset』] = 『stix』
plt.rcParams[『font.size』] = 12
plt.rcParams[『axes.linewidth』] = 1.2

# 创建 H=ts 曲面数据（更精细的网格）
S_plane = np.linspace(-200, 200, 100)
T_plane = np.linspace(100, 500, 100)
S_plane_grid, T_plane_grid = np.meshgrid(S_plane, T_plane)
H_plane_grid = T_plane_grid * S_plane_grid / 1000  # H (kJ/mol)

# 创建图形
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection=『3d』)

# 绘制 H=ts 曲面（MATLAB 风格）
from matplotlib import cm

# 计算 G 值用于颜色映射
G_plane = H_plane_grid * 1000 - T_plane_grid * S_plane_grid  # G (J/mol)

# 使用 MATLAB 风格的曲面渲染
surf = ax.plot_surface(H_plane_grid, S_plane_grid, T_plane_grid, 
                       cmap=cm.jet,  # MATLAB 默认色彩映射
                       linewidth=0.5, 
                       antialiased=True,
                       alpha=0.8,
                       rstride=2, cstride=2)  # 控制网格密度

# 添加颜色条
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20, pad=0.1)
cbar.set_label(『Temperature T (K)』, fontsize=12)

# 设置坐标轴标签（包含单位）
ax.set_xlabel(『Enthalpy H (kJ/mol)』, fontsize=14, labelpad=15)
ax.set_ylabel(『Entropy S (J/mol·K)』, fontsize=14, labelpad=15)
ax.set_zlabel(『Temperature T (K)』, fontsize=14, labelpad=15)

# 设置标题
ax.set_title(『Gibbs Free Energy G = H - ts』, 
             fontsize=16, pad=25, weight=『bold』)

# 创建图例（简洁的 G=0）
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=『blue』, alpha=0.8, label=『G = 0』)
]
ax.legend(handles=legend_elements, loc=『upper left』, fontsize=12)

# 设置视角
ax.view_init(elev=25, azim=45)

# 设置网格
ax.grid(True, alpha=0.3)

# 设置坐标轴范围
ax.set_xlim([-100, 100])
ax.set_ylim([-200, 200])
ax.set_zlim([100, 500])

# 设置刻度
ax.set_xticks(np.arange(-100, 101, 50))
ax.set_yticks(np.arange(-200, 201, 100))
ax.set_zticks(np.arange(100, 501, 100))

# 美化图形
ax.tick_params(axis=『both』, which=『major』, labelsize=11)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor(『white』)
ax.yaxis.pane.set_edgecolor(『white』)
ax.zaxis.pane.set_edgecolor(『white』)

# 调整布局并保存
plt.tight_layout()
plt.savefig(『gibbs_free_energy_3d_plot.png』, dpi=300, bbox_inches=『tight』, 
            facecolor=『white』, edgecolor=『none』)
plt.savefig(『gibbs_free_energy_3d_plot.pdf』, bbox_inches=『tight』, 
            facecolor=『white』, edgecolor=『none』)

plt.show()

print(「吉布斯自由能三维图创建成功！」)
print(「图像已保存为: gibbs_free_energy_3d_plot.png 和 gibbs_free_energy_3d_plot.pdf」)
print(「\n 图例说明:」)
print(「- H = ts 曲面: 使用 MATLAB 风格的 jet 色彩映射显示吉布斯自由能」)
print(「\n 坐标轴单位:」)
print(「- 焓 H: kJ/mol」)
print(「- 熵 S: J/mol·K」) 
print(「- 温度 T: K」)
print(「\n 颜色条说明:」)
print(「- 颜色条显示吉布斯自由能 G 的值 (J/mol)」)
print(「- 红色区域表示 G > 0 (反应逆向)」)
print(「- 蓝色区域表示 G < 0 (反应正向)」)
print(「\n 交互功能:」)
print(「- 在显示的图形窗口中，可以使用鼠标旋转查看不同角度」)
print(「- 支持缩放和平移操作」)
print(「- 可以调整视角以获得最佳视觉效果」)