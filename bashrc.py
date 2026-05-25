# Подключаем git prompt helper
source /usr/lib/git-core/git-sh-prompt

# Показывать '*' если есть незакоммиченные изменения
export GIT_PS1_SHOWDIRTYSTATE=1

# Цветной prompt с git branch/hash
# export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 " git:(%s)")\$ '
# export PS1="\W ($(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ "
# export PS1='\[\033[01;34m\]\W\[\033[00m\]$(__git_ps1 " (\[\033[01;31m\]%s\[\033[00m\])") \$ ' # Это хороший вариант
parse_git_branch() {
  # Получаем название ветки
  local branch=$(__git_ps1 "%s")

  # Если ветки нет, ничего не выводим
  [ -z "$branch" ] && return

  # Цветовые коды,```

### Что обернутые в \001 и \002 для корректного расчета длины строки
  local blue="\001\033[01;34m\002"
  local red="\001\033[01;31m\002"
  local reset="\001\033[00m\002"

  if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
    printf "${blue}(%s)${reset}" "$branch"
  else
    printf "${red}(%s)${reset}" "$branch"
  fi
}

# В самом PS1 не забывай пробелы и обертки
export PS1='\[\033[01;34m\]\W\[\033[00m\] $(parse_git_branch) \$ '