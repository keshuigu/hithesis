# LaTeX Beamer博士答辩PPT Makefile

# 主目标文件
TARGET = defense_presentation
TEX_FILE = $(TARGET).tex
PDF_FILE = $(TARGET).pdf

# 编译器设置
LATEX = xelatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error

# 默认目标
.PHONY: all clean distclean help view

all: $(PDF_FILE)

# 编译PPT
$(PDF_FILE): $(TEX_FILE)
	@echo "正在编译博士答辩PPT..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "编译完成: $(PDF_FILE)"

# 查看PPT
view: $(PDF_FILE)
	@if command -v evince >/dev/null 2>&1; then \
		evince $(PDF_FILE) & \
	elif command -v okular >/dev/null 2>&1; then \
		okular $(PDF_FILE) & \
	elif command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $(PDF_FILE) & \
	else \
		echo "请手动打开文件: $(PDF_FILE)"; \
	fi

# 清理临时文件
clean:
	@echo "清理临时文件..."
	@rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fls *.fdb_latexmk *.synctex.gz
	@echo "临时文件清理完成"

# 完全清理
distclean: clean
	@echo "删除生成的PDF文件..."
	@rm -f $(PDF_FILE)
	@echo "完全清理完成"

# 连续编译模式（用于开发）
watch:
	@echo "进入连续编译模式，按Ctrl+C退出..."
	@while inotifywait -e modify $(TEX_FILE) 2>/dev/null; do \
		echo "检测到文件变化，重新编译..."; \
		make $(PDF_FILE); \
	done

# 帮助信息
help:
	@echo "LaTeX博士答辩PPT编译工具"
	@echo ""
	@echo "可用目标："
	@echo "  all        - 编译PPT（默认）"
	@echo "  view       - 编译并查看PPT"
	@echo "  clean      - 清理临时文件"
	@echo "  distclean  - 完全清理（包括PDF）"
	@echo "  watch      - 连续编译模式（需要inotify-tools）"
	@echo "  help       - 显示此帮助信息"
	@echo ""
	@echo "使用示例："
	@echo "  make              # 编译PPT"
	@echo "  make view         # 编译并查看"
	@echo "  make clean        # 清理临时文件"

# 检查依赖
check-deps:
	@echo "检查编译环境..."
	@which xelatex >/dev/null || (echo "错误: 未找到xelatex编译器" && exit 1)
	@echo "✓ XeLaTeX编译器可用"
	@xelatex --version | head -1
	@echo "环境检查完成"

# 安装依赖提示
install-deps:
	@echo "安装LaTeX环境的建议："
	@echo ""
	@echo "Ubuntu/Debian:"
	@echo "  sudo apt-get install texlive-full texlive-xetex"
	@echo ""
	@echo "CentOS/RHEL:"
	@echo "  sudo yum install texlive texlive-xetex"
	@echo ""
	@echo "MacOS:"
	@echo "  brew install --cask mactex"
	@echo ""
	@echo "Windows:"
	@echo "  下载并安装 MiKTeX 或 TeX Live"

.PHONY: check-deps install-deps watch