# Makefile for Beamer presentation compilation

# 主文件名（不含扩展名）
MAIN = presentation

# LaTeX 编译器
LATEX = xelatex

# BibTeX 编译器
BIBTEX = bibtex

# 编译选项
LATEXOPT = -shell-escape -interaction=nonstopmode -file-line-error

# 输出目录
OUTDIR = .

# 临时文件扩展名
TEMP_EXT = aux log out toc nav snm vrb bbl blg

.PHONY: all clean distclean view

# 默认目标：编译演示文稿
all: $(MAIN).pdf

# 编译 PDF（完整编译流程）
$(MAIN).pdf: $(MAIN).tex
	@echo "正在编译演示文稿..."
	$(LATEX) $(LATEXOPT) $(MAIN)
	@echo "第一次编译完成"
	$(LATEX) $(LATEXOPT) $(MAIN)
	@echo "第二次编译完成"
	@echo "编译完成: $(MAIN).pdf"

# 快速编译（单次，适合调试）
quick: $(MAIN).tex
	@echo "快速编译模式..."
	$(LATEX) $(LATEXOPT) $(MAIN)

# 使用 latexmk 自动编译（如果可用）
auto:
	@echo "使用 latexmk 自动编译..."
	latexmk -xelatex -synctex=1 -interaction=nonstopmode $(MAIN).tex

# 清理临时文件
clean:
	@echo "清理临时文件..."
	@for ext in $(TEMP_EXT); do \
		rm -f $(MAIN).$$ext; \
	done
	@rm -f *.fls *.fdb_latexmk *.synctex.gz
	@echo "清理完成"

# 完全清理（包括 PDF）
distclean: clean
	@echo "删除生成的 PDF 文件..."
	@rm -f $(MAIN).pdf
	@echo "完全清理完成"

# 查看 PDF
view: $(MAIN).pdf
	@echo "打开 PDF 文件..."
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(MAIN).pdf & \
	elif command -v open > /dev/null; then \
		open $(MAIN).pdf & \
	elif command -v evince > /dev/null; then \
		evince $(MAIN).pdf & \
	else \
		echo "未找到 PDF 查看器"; \
	fi

# 显示帮助信息
help:
	@echo "可用的 make 目标："
	@echo "  all (默认)  - 完整编译演示文稿"
	@echo "  quick       - 快速编译（单次）"
	@echo "  auto        - 使用 latexmk 自动编译"
	@echo "  clean       - 清理临时文件"
	@echo "  distclean   - 完全清理（包括 PDF）"
	@echo "  view        - 查看生成的 PDF"
	@echo "  help        - 显示此帮助信息"
