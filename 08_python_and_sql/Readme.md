2019-03-01

A mai alkalmon én (Balogh Balázs) és Berci tartottunk egy-egy workshopot illetve előadást.
Részemről az SQL volt a főszerepben, készítettünk egy SQLite motort, illetve egy táblát amibe Pythonból beinsertáltuk az internetről ingyenesen elérhető BKK_GTFS adatbázisból az összes BKK megálló koordinátáját és nevét.
Ebből a táblából visszanyertük az adatokat pandas dataframe-be, amiből csináltunk egy folium térképet, és MarkerClustert alkalmazva (hogy az 5800 pont szépen, és performancia barátan jelenjen meg) rátettük a megállókat.

Eztán Berci következett, haladtunk tovább a 105-ös Pandas Cookbook résszel, ahol is a DataFrameből való szelektálást néztük meg, egy az amerikai egyetemeket összefoglaló listán, összevetve SQL WHERE feltételével. A Cookbookok, mint mindig, a Pandas_Cookbook repoban érhetőek el.