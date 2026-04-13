import pandas as pd
import os
import re

class ExcelDataManager:
    def __init__(self):
        self.file_path = "data/attractions.xlsx"
        self.df = None
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            print(f"Файл {self.file_path} не найден!")
            return
        try:
            # Загружаем Excel. Убедитесь, что лист называется 'Лист1'
            self.df = pd.read_excel(self.file_path, sheet_name='Лист1').fillna("")
            
            # Приводим названия колонок к стандарту
            mapping = {
                'Name_ru': 'name_ru', 
                'Name_en': 'name_en',
                'Description_ru': 'description_ru', 
                'Description_en': 'description_en',
                'Address_ru': 'address_ru',
                'Address_en': 'address_en',
                'Photo': 'photo',
                'Metro': 'station_ru'
            }
            self.df.rename(columns=mapping, inplace=True)
            self.df['station_ru'] = self.df['station_ru'].astype(str).str.strip()
        except Exception as e:
            print(f"Ошибка загрузки Excel: {e}")

    def get_attractions_by_station(self, station_name, language="ru"):
        if self.df is None:
            self.load_data()
        
        # Очищаем название станции от цифр (например "1. Баррикадная")
        target = re.sub(r'^\d+\.\s*', '', str(station_name)).lower().strip()
        mask = self.df['station_ru'].str.lower().str.contains(target, na=False)
        
        results = []
        for idx, row in self.df[mask].iterrows():
            name = row.get(f'name_{language}', row.get('name_ru', 'Unknown'))
            results.append({"id": idx, "name": name})
        return results

    def get_details_by_id(self, row_id, language="ru"):
        if self.df is None:
            self.load_data()
        try:
            row = self.df.loc[int(row_id)]
            return {
                "name": row.get(f'name_{language}', row.get('name_ru', '')),
                "description": row.get(f'description_{language}', row.get('description_ru', '')),
                "address": row.get(f'address_{language}', row.get('address_ru', '')),
                "photo": row.get('photo', '')
            }
        except Exception:
            return None

excel_manager = ExcelDataManager()