# districts_data.py

DISTRICTS = {
    "CAO": {
        "name": {"ru": "Центральный (ЦАО)", "en": "Central (CAO)"},
        "stations": {
            "ru": [
                "Александровский сад", "Арбатская", "Баррикадная", "Бауманская", "Белорусская",
                "Библиотека имени Ленина", "Боровицкая", "Воробьёвы горы", "Деловой центр",
                "Добрынинская", "Достоевская", "Китай-город", "Комсомольская", "Краснопресненская",
                "Красносельская", "Красные ворота", "Крестьянская застава", "Кропоткинская",
                "Кузнецкий мост", "Курская", "Лубянка", "Лужники", "Марксистская",
                "Маяковская", "Менделеевская", "Москва-Сити", "Новокузнецкая", "Новослободская",
                "Октябрьская", "Охотный ряд", "Павелецкая", "Парк культуры", "Площадь Ильича",
                "Площадь Революции", "Полянка", "Пролетарская", "Проспект мира", "Пушкинская",
                "Рижская", "Римская", "Серпуховская", "Смоленская", "Спортивная", "Сретенский бульвар",
                "Сухаревская", "Таганская", "Тверская", "Театральная", "Третьяковская", "Трубная",
                "Тургеневская", "Улица 1905 года", "Фрунзенская", "Цветной бульвар", "Чеховская",
                "Чистые пруды", "Чкаловская", "Шелепиха"
            ],
            "en": [
                "Alexandrovsky Sad", "Arbatskaya", "Barrikadnaya", "Baumanskaya", "Belorusskaya",
                "Biblioteka Imeni Lenina", "Borovitskaya", "Vorobyovy Gory", "Delovoy Tsentr",
                "Dobryninskaya", "Dostoyevskaya", "Kitay-Gorod", "Komsomolskaya", "Krasnopresnenskaya",
                "Krasnoselskaya", "Krasnye Vorota", "Krestyanskaya Zastava", "Kropotkinskaya",
                "Kuznetsky Most", "Kurskaya", "Lubyanka", "Luzhniki", "Marksistskaya",
                "Mayakovskaya", "Mendeleyevskaya", "Moskva-City", "Novokuznetskaya", "Novoslobodskaya",
                "Oktyabrskaya", "Okhotny Ryad", "Paveletskaya", "Park Kultury", "Ploshchad Ilicha",
                "Ploshchad Revolyutsii", "Polyanka", "Proletarskaya", "Prospekt Mira", "Pushkinskaya",
                "Rizhskaya", "Rimskaya", "Serpukhovskaya", "Smolenskaya", "Sportivnaya", "Sretensky Bulvar",
                "Sukharevskaya", "Taganskaya", "Tverskaya", "Teatralnaya", "Tretyakovskaya", "Trubnaya",
                "Turgenevskaya", "Ulitsa 1905 Goda", "Frunzenskaya", "Tsvetnoy Bulvar", "Chekhovskaya",
                "Chistye Prudy", "Chkalovskaya", "Shelepikha"
            ]
        }
    },
    "SAO": {
        "name": {"ru": "Северный (САО)", "en": "Northern (SAO)"},
        "stations": {
            "ru": [
                "Аэропорт", "Балтийская", "Беговая", "Беломорская", "Верхние Лихоборы",
                "Водный стадион", "Войковская", "Динамо", "Дмитровская", "Зорге",
                "Коптево", "Лихоборы", "Окружная", "Петровский парк",
                "Петровско-Разумовская", "Полежаевская", "Речной вокзал", "Селигерская",
                "Сокол", "Тимирязевская", "Ховрино", "Хорошёвская", "ЦСКА", "Яхромская"
            ],
            "en": [
                "Aeroport", "Baltiyskaya", "Begovaya", "Belomorskaya", "Verkhniye Likhobory",
                "Vodny Stadion", "Voykovskaya", "Dinamo", "Dmitrovskaya", "Zorge",
                "Koptevo", "Likhobory", "Okruzhnaya", "Petrovsky Park",
                "Petrovsko-Razumovskaya", "Polezhayevskaya", "Rechnoy Vokzal", "Seligerskaya",
                "Sokol", "Timiryazevskaya", "Khovrino", "Khoroshyovskaya", "CSKA", "Yakhromskaya"
            ]
        }
    },
    "SVAO": {
        "name": {"ru": "Северо-Восточный (СВАО)", "en": "North-Eastern (SVAO)"},
        "stations": {
            "ru": [
                "Алексеевская", "Алтуфьево", "Бабушкинская", "Бибирево", "Ботанический сад",
                "Бутырская", "ВДНХ", "Владыкино", "Дмитровская", "Лианозово", "Марьина роща",
                "Медведково", "Окружная", "Отрадное", "Ростокино", "Савёловская",
                "Свиблово", "Физтех", "Фонвизинская"
            ],
            "en": [
                "Alexeyevskaya", "Altufyevo", "Babushkinskaya", "Bibirevo", "Botanichesky Sad",
                "Butyrskaya", "VDNKh", "Vladykino", "Dmitrovskaya", "Lianozovo", "Maryina Roshcha",
                "Medvedkovo", "Okruzhnaya", "Otradnoye", "Rostokino", "Savyolovskaya",
                "Sviblovo", "Phystech", "Fonvizinskaya"
            ]
        }
    },
    "VAO": {
        "name": {"ru": "Восточный (ВАО)", "en": "Eastern (VAO)"},
        "stations": {
            "ru": [
                "Белокаменная", "Бульвар Рокоссовского", "Выхино", "Измайловская", "Локомотив",
                "Лухмановская", "Новогиреево", "Новокосино", "Партизанская", "Перово",
                "Преображенская площадь", "Семёновская", "Соколиная Гора", "Сокольники",
                "Улица Дмитриевского", "Черкизовская", "Шоссе Энтузиастов", "Щёлковская", "Электрозаводская"
            ],
            "en": [
                "Belokamennaya", "Bulvar Rokossovskogo", "Vykhino", "Izmaylovskaya", "Lokomotiv",
                "Lukhmanovskaya", "Novogireyevo", "Novokosino", "Partizanskaya", "Perovo",
                "Preobrazhenskaya Ploshchad", "Semyonovskaya", "Sokolinaya Gora", "Sokolniki",
                "Ulitsa Dmitriyevskogo", "Cherkizovskaya", "Shosse Entuziastov", "Shchyolkovskaya", "Elektrozavodskaya"
            ]
        }
    },
    "YUVAO": {
        "name": {"ru": "Юго-Восточный (ЮВАО)", "en": "South-Eastern (YUVAO)"},
        "stations": {
            "ru": [
                "Авиамоторная", "Андроновка", "Братиславская", "Волгоградский проспект",
                "Волжская", "Дубровка", "Жулебино", "Кожуховская", "Косино", "Котельники",
                "Кузьминки", "Лермонтовский проспект", "Лефортово", "Люблино", "Марьино",
                "Некрасовка", "Нижегородская", "Новохохловская", "Окская", "Печатники",
                "Рязанский проспект", "Стахановская", "Текстильщики", "Угрешская", "Юго-Восточная"
            ],
            "en": [
                "Aviamotornaya", "Andronovka", "Bratislavskaya", "Volgogradsky Prospekt",
                "Volzhskaya", "Dubrovka", "Zhulebino", "Kozhukhovskaya", "Kosino", "Kotelniki",
                "Kuzminki", "Lermontovsky Prospekt", "Lefortovo", "Lyublino", "Maryino",
                "Nekrasovka", "Nizhegorodskaya", "Novokhokhlovskaya", "Okskaya", "Pechatniki",
                "Ryazansky Prospekt", "Stakhanovskaya", "Tekstilschiki", "Ugreshskaya", "Yugo-Vostochnaya"
            ]
        }
    },
    "YUAO": {
        "name": {"ru": "Южный (ЮАО)", "en": "Southern (YUAO)"},
        "stations": {
            "ru": [
                "Автозаводская", "Алма-Атинская", "Аннино", "Борисово", "Варшавская",
                "Верхние Котлы", "Домодедовская", "ЗИЛ", "Зябликово", "Кантемировская",
                "Каширская", "Кленовый бульвар", "Коломенская", "Красногвардейская",
                "Ленинский проспект", "Лесопарковая", "Нагатинская", "Нагатинский затон",
                "Нагорная", "Орехово", "Пражская", "Технопарк", "Тульская",
                "Улица академика Янгеля", "Царицыно", "Шаболовская", "Шипиловская", "Южная"
            ],
            "en": [
                "Avtozavodskaya", "Alma-Atinskaya", "Annino", "Borisovo", "Varshavskaya",
                "Verkhniye Kotly", "Domodedovskaya", "ZIL", "Zyablikovo", "Kantemirovskaya",
                "Kashirskaya", "Klenoviy Bulvar", "Kolomenskaya", "Krasnogvardeyskaya",
                "Leninskiy Prospekt", "Lesoparkovaya", "Nagatinskaya", "Nagatinskiy Zaton",
                "Nagornaya", "Orekhovo", "Prazhskaya", "Tekhnopark", "Tulskaya",
                "Ulitsa Akademika Yangelya", "Tsaritsyno", "Shabolovskaya", "Shipilovskaya", "Yuzhnaya"
            ]
        }
    },
    "ZAO": {
        "name": {"ru": "Западный (ЗАО)", "en": "Western (ZAO)"},
        "stations": {
            "ru": [
                "Аминьевская", "Багратионовская", "Боровское шоссе", "Говорово", "Давыдково",
                "Киевская", "Крылатское", "Кунцевская", "Кутузовская", "Ломоносовский проспект",
                "Минская", "Мичуринский проспект", "Молодёжная", "Мякинино", "Новаторская",
                "Новопеределкино", "Озерная", "Парк Победы", "Пионерская", "Проспект Вернадского",
                "Раменки", "Славянский бульвар", "Солнцево", "Студенческая", "Тропарево",
                "Университет", "Филёвский парк", "Фили", "Юго-Западная"
            ],
            "en": [
                "Aminyevskaya", "Bagrationovskaya", "Borovskoye Shosse", "Govorovo", "Davydkovo",
                "Kievskaya", "Krylatskoye", "Kuntsevskaya", "Kutuzovskaya", "Lomonosovsky Prospekt",
                "Minskaya", "Michurinsky Prospekt", "Molodyozhnaya", "Myakinino", "Novatorskaya",
                "Novoperedelkino", "Ozyornaya", "Park Pobedy", "Pionerskaya", "Prospekt Vernadskogo",
                "Ramenki", "Slavyansky Bulvar", "Solntsevo", "Studencheskaya", "Troparyovo",
                "Universitet", "Filyovsky Park", "Fili", "Yugo-Zapadnaya"
            ]
        }
    },
    "SZAO": {
        "name": {"ru": "Северо-Западный (СЗАО)", "en": "North-Western (SZAO)"},
        "stations": {
            "ru": [
                "Волоколамская", "Митино", "Мнёвники", "Народное ополчение", "Октябрьское поле",
                "Панфиловская", "Планерная", "Пятницкое шоссе", "Спартак", "Стрешнево",
                "Строгино", "Сходненская", "Терехово", "Тушинская", "Щукинская"
            ],
            "en": [
                "Volokolamskaya", "Mitino", "Mnyovniki", "Narodnoye Opolcheniye", "Oktyabrskoye Pole",
                "Panfilovskaya", "Planernaya", "Pyatnitskoye Shosse", "Spartak", "Streshnevo",
                "Strogino", "Skhodnenskaya", "Terekhovo", "Tushinskaya", "Shchukinskaya"
            ]
        }
    },
    "YUZAO": {
        "name": {"ru": "Юго-Западный (ЮЗАО)", "en": "South-Western (YUZAO)"},
        "stations": {
            "ru": [
                "Академическая", "Беляево", "Битцевский парк", "Бульвар адмирала Ушакова",
                "Бульвар Дмитрия Донского", "Бунинская аллея", "Вавиловская", "Воронцовская",
                "Генерала Тюленева", "Зюзино", "Калужская", "Каховская", "Коньково", "Крымская",
                "Ленинский проспект", "Нахимовский проспект", "Новаторская", "Новоясеневская",
                "Новые Черёмушки", "Площадь Гагарина", "Профсоюзная", "Севастопольская",
                "Тёплый стан", "Улица Горчакова", "Улица Скобелевская", "Улица Старокачаловская",
                "Университет", "Университет дружбы народов", "Чертановская", "Ясенево"
            ],
            "en": [
                "Akademicheskaya", "Belyayevo", "Bitsevsky Park", "Bulvar Admirala Ushakova",
                "Bulvar Dmitriya Donskogo", "Buninskaya Alleya", "Vavilovskaya", "Vorontsovskaya",
                "Generala Tyuleneva", "Zyuzino", "Kaluzhskaya", "Kakhovskaya", "Konkovo", "Krymskaya",
                "Leninskiy Prospekt", "Nakhimovskiy Prospekt", "Novatorskaya", "Novoyasenevskaya",
                "Novye Cheryomushki", "Ploshchad Gagarina", "Profsoyuznaya", "Sevastopolskaya",
                "Tyoply Stan", "Ulitsa Gorchakova", "Ulitsa Skobelevskaya", "Ulitsa Starokachalovskaya",
                "Universitet", "Peoples' Friendship University", "Chertanovskaya", "Yasenevo"
            ]
        }
    },
    "NAO": {
        "name": {"ru": "Новомосковский (НАО)", "en": "Novomoskovsky (NAO)"},
        "stations": {
            "ru": [
                "Аэропорт Внуково", "Коммунарка", "Корниловская", "Новомосковская", "Ольховая",
                "Потапово", "Прокшино", "Пыхтино", "Рассказовка", "Румянцево", "Саларьево",
                "Тютчевская", "Филатов Луг", "Щербинка"
            ],
            "en": [
                "Vnukovo Airport", "Kommunarka", "Kornilovskaya", "Novomoskovskaya", "Olkhovaya",
                "Potapovo", "Prokshino", "Pykhtino", "Rasskazovka", "Rumyantsevo", "Salaryevo",
                "Tyutchevskaya", "Filatov Lug", "Shcherbinka"
            ]
        }
    }
}