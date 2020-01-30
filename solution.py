import pandas as pd
import numpy as np

#В jupiter notebook более наглядно

spend = pd.read_csv('./in_data_p.csv')
downloads = pd.read_csv('./in_data_a.csv') 

spend.rename(columns={'date': 'Date'}, inplace=True)

# Две таблицы можно соединить по полям Date и ad_id n
# Соединяем с помощью full join
all_data = spend.merge(downloads, on=['Date', 'ad_id'], how='outer')

out = all_data.groupby(['Date', 'app', 'Campaign', 'os']).agg(
    {'spend': 'sum', 'Installs': 'sum'}) #Делаем итоговую таблицу out суммируя траты и установки

# Создаем столбец, показывающий эффективность рекламы
out['cpi'] = out['spend']/out['Installs']

# Заменяем пустые значения и бесконечности образовавшиеся вследствии деления на ноль(скачиваний)
out['cpi'].replace([np.inf, np.NaN], 0, inplace=True)

out.to_csv('./out.csv', sep='\t')  # Записываем в файл
