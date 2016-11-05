# 起動コマンドをMakefileで記述してsupervisorで起動すると停止時にZombieになる問題

`manage.py runserver` は異常終了時の処理が甘いため発生する問題。gnu makeは全く悪くなかった。
supervisorで管理するのであれば、gunicornを使うのが良さそう。
