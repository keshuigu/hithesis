#!/bin/bash

# 博士答辩PPT编译脚本
# 用于快速编译和预览PPT

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
TEX_FILE="defense_presentation.tex"
PDF_FILE="defense_presentation.pdf"
LATEX_CMD="xelatex"

# 打印带颜色的消息
print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# 检查依赖
check_dependencies() {
    print_message $BLUE "检查编译环境..."

    if ! command -v $LATEX_CMD &> /dev/null; then
        print_message $RED "错误: 未找到 $LATEX_CMD 编译器"
        print_message $YELLOW "请安装 TeX Live 或 MiKTeX"
        exit 1
    fi

    if [ ! -f "$TEX_FILE" ]; then
        print_message $RED "错误: 未找到源文件 $TEX_FILE"
        exit 1
    fi

    print_message $GREEN "✓ 环境检查通过"
}

# 编译PPT
compile_ppt() {
    print_message $BLUE "开始编译博士答辩PPT..."

    # 第一次编译
    print_message $YELLOW "第一次编译..."
    $LATEX_CMD -interaction=nonstopmode -halt-on-error "$TEX_FILE"

    # 第二次编译（处理引用和目录）
    print_message $YELLOW "第二次编译..."
    $LATEX_CMD -interaction=nonstopmode -halt-on-error "$TEX_FILE"

    if [ $? -eq 0 ]; then
        print_message $GREEN "✓ 编译成功: $PDF_FILE"
    else
        print_message $RED "✗ 编译失败"
        exit 1
    fi
}

# 清理临时文件
clean_files() {
    print_message $BLUE "清理临时文件..."
    rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fls *.fdb_latexmk *.synctex.gz
    print_message $GREEN "✓ 临时文件清理完成"
}

# 查看PPT
view_ppt() {
    if [ -f "$PDF_FILE" ]; then
        print_message $BLUE "打开PPT文件..."

        if command -v evince &> /dev/null; then
            evince "$PDF_FILE" &
        elif command -v okular &> /dev/null; then
            okular "$PDF_FILE" &
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$PDF_FILE" &
        else
            print_message $YELLOW "请手动打开文件: $PDF_FILE"
        fi
    else
        print_message $RED "错误: 未找到PDF文件，请先编译"
    fi
}

# 显示帮助
show_help() {
    cat << EOF
博士答辩PPT编译脚本

用法: $0 [选项]

选项:
    compile, c      编译PPT
    view, v         查看PPT
    clean           清理临时文件
    distclean       完全清理（包括PDF）
    check           检查编译环境
    help, h         显示此帮助信息

示例:
    $0 compile      # 编译PPT
    $0 view         # 查看PPT
    $0 clean        # 清理临时文件

EOF
}

# 主函数
main() {
    case "${1:-compile}" in
        compile|c)
            check_dependencies
            compile_ppt
            ;;
        view|v)
            check_dependencies
            compile_ppt
            view_ppt
            ;;
        clean)
            clean_files
            ;;
        distclean)
            clean_files
            if [ -f "$PDF_FILE" ]; then
                rm -f "$PDF_FILE"
                print_message $GREEN "✓ PDF文件已删除"
            fi
            ;;
        check)
            check_dependencies
            ;;
        help|h)
            show_help
            ;;
        *)
            print_message $RED "错误: 未知选项 '$1'"
            show_help
            exit 1
            ;;
    esac
}

# 运行主函数
main "$@"