# All spoken lines of the game: (id, speaker, spoken text[, Czech subtitle]) and the guards' barks.
# Used by make_voices.py (offline Piper TTS) and make_voices_neural.py (Microsoft neural voices via edge-tts).
LINES = [
    # intro: capture in the woods
    ('bj_01', 'bj', 'Tady Orel. Jsem na místě. Hrad Grimhold je hned za hřebenem.'),
    ('lon_01', 'lon', 'Rozumím, Orle. Buďte opatrný. Hory jsou plné hlídek.'),
    ('off_01', 'offA', 'Hände hoch! Keine Bewegung!', 'Ruce vzhůru! Ani hnout!'),
    ('off_02', 'off', 'Ein amerikanischer Spion. Ganz allein in unseren Bergen.', 'Americký špion. Úplně sám v našich horách.'),
    ('bj_02', 'bj', 'Jen jsem si tu sbíral houby.'),
    ('off_03', 'offM', 'Der Doktor wird sich freuen. Bringt ihn nach Grimhold!', 'Doktor bude mít radost. Odveďte ho na Grimhold!'),
    # intro: the cell
    ('grd_01', 'grd', 'Aufstehen, Ami! Der Doktor will dich sehen.', 'Vstávej, Amíku! Doktor tě chce vidět.'),
    ('bj_03', 'bj', 'Doktor si bude muset počkat.'),
    ('bj_04', 'bj', 'Revolver a klíče. A teď ven z téhle díry.'),
    # episode 2: down the cable car
    ('bj_05', 'bj', 'Londýne, tady Orel. Jsem venku z Grimholdu. Mám plány i Zemanův deník.'),
    ('lon_02', 'lon', 'Výborně, Orle. A co je v tom deníku?'),
    ('bj_06', 'bj', 'Wolfsgrund. Podzemní továrna, kam vede jen železnice. Tam stavějí Finsternis.'),
    ('lon_03', 'lon', 'Pak tam musíte vy. Spojka odboje na vás čeká v hájovně nad údolím. Hodně štěstí.'),
    ('bj_07', 'bj', 'Štěstí si nechte, plukovníku. Mně stačí náboje.'),
    # episode 3: the ramp at Wolfsgrund
    ('zem_01', 'zem', 'Der Übersoldat Mark Zwei ist bereit, Standartenführer. Wir müssen ihn nur noch wecken.', 'Übersoldat Mk II je připraven, Standartenführere. Stačí ho jen probudit.'),
    ('off_04', 'off', 'Und die Raketen, Herr Doktor?', 'A rakety, pane doktore?'),
    ('zem_02', 'zem', 'In drei Tagen fliegt die erste nach London.', 'Za tři dny poletí první na Londýn.'),
    ('bj_08', 'bj', 'Za tři dny. To mám času dost.'),
    # finale
    ('lon_04', 'lon', 'Orle, tady Londýn. Slyšíte nás? Seismografy ve Švýcarsku právě zaznamenaly zemětřesení.'),
    ('bj_09', 'bj', 'To nebylo zemětřesení, Londýne. To byl Wolfsgrund. Operace Finsternis skončila.'),
    ('lon_05', 'lon', 'Skvělá práce, Orle. Je čas vrátit se domů.'),
    ('bj_10', 'bj', 'Domů. To zní dobře.'),
    # in-game: Zeman and B.J.
    ('zem_03', 'zem', 'Wachen! Haltet ihn auf!', 'Stráže! Zastavte ho!'),
    ('bj_obj1', 'bj', 'Mám to.'), ('bj_obj2', 'bj', 'Další odškrtnuto.'), ('bj_obj3', 'bj', 'Tohle se bude v Londýně hodit.'),
]
BARKS = {
    'sus': [('Was war das?', 'surprised'), ('Hallo? Ist da jemand?', 'surprised'), ('Hm? Wer ist da?', 'neutral'), ('Da hat sich was bewegt.', 'neutral')],
    'alert': [('Alarm!', 'angry'), ('Da ist er!', 'angry'), ('Halt! Stehen bleiben!', 'angry'), ('Feind gesichtet!', 'angry')],
    'body': [('Mein Gott, ein Toter!', 'surprised'), ('Hier liegt einer! Alarm!', 'angry')],
    'lost': [('Nichts. Muss der Wind gewesen sein.', 'neutral'), ('Nur eine Ratte.', 'neutral'), ('Ich sehe niemanden.', 'neutral')],
}

# ---- expansion "Blázen z Londýna: Zajetí Orla": Gefreiter Brandt, Feldwebel Krüger and the squad (German, Czech subtitles), the Eagle (Czech)
LINES_ZO = [
    # intro: the guardroom
    ('zo_i1', 'kes', 'Hast du das gehört? Schüsse! Unten in den Kerkern.', 'Slyšels to? Střelba! Dole v kobkách.'),
    ('zo_i2', 'brn', 'Ruhig, Kessler. Bestimmt nur ein Gefangener, der Ärger macht.', 'Klid, Kesslere. Určitě jen nějaký vězeň dělá potíže.'),
    ('zo_i3', 'bj', 'Promiň, kamaráde. Nic osobního.'),
    ('zo_i4', 'brn', 'Der Adler. Ich finde dich.', 'Orel… Najdu tě…'),
    # 1.1 the castle
    ('zo_101', 'brn', 'Kessler? Vogt? Tot. Beide tot. Und ich lebe noch.', 'Kesslere? Vogte? … Mrtví. Oba. A já pořád žiju.'),
    ('zo_102', 'lsp', 'Achtung! Achtung! Die Gefangenen sind frei! Alle Männer zur Waffenkammer! Feldwebel Krüger sammelt im Hof!', 'Pozor! Pozor! Vězni jsou na svobodě! Všichni muži do zbrojnice! Feldwebel Krüger svolává na nádvoří!'),
    ('zo_j1', 'mul', 'Brandt! Du lebst! Ich dachte, die hätten dich erwischt. Ich komme mit.', 'Brandte! Ty žiješ! Myslel jsem, že tě dostali. Jdu s tebou.'),
    ('zo_j2', 'web', 'Endlich! Diese Gefangenen sind überall. Ich bin dabei.', 'Konečně! Ti vězni jsou všude. Jdu do toho.'),
    ('zo_j3', 'hof', 'Jawohl, Brandt. Ich folge dir.', 'Rozkaz, Brandte. Jdu za tebou.'),
    ('zo_kw', 'krg', 'Brandt! Wo sind Ihre Männer? Holen Sie sie, dann reden wir.', 'Brandte! Kde máte své muže? Přiveďte je, pak si promluvíme.'),
    ('zo_103', 'krg', 'Brandt. Gut, dass Sie leben. Der Amerikaner will zur Seilbahn. Wir holen ihn uns. Mir nach!', 'Brandte. Dobře, že žijete. Ten Američan chce k lanovce. Dostaneme ho. Za mnou!'),
    ('zo_104', 'mul', 'Der Feldwebel wartet im Hof. Gehen wir.', 'Feldwebel čeká na nádvoří. Jdeme.'),
    # 1.2 the top station
    ('zo_201', 'krgA', 'Über die Mauer und durch den Turm zur Bergstation. Bewegung!', 'Přes hradby a věží k horní stanici. Pohyb!'),
    ('zo_206', 'krgA', 'Partisanen auf den Mauern! Sie sind gekommen, um ihn zu holen!', 'Partyzáni na hradbách! Přišli si pro něj!'),
    ('zo_202', 'krgA', 'Da! In der Kabine! Feuer! Feuer!', 'Tamhle! V kabině! Pal! Pal!'),
    ('zo_204', 'krg', 'Verdammt! Er ist weg. Brandt, holen Sie die zweite Kabine! Der Hebel im Maschinenhaus!', 'Sakra! Je pryč. Brandte, přivolejte druhou kabinu! Páka ve strojovně!'),
    ('zo_205', 'krg', 'Die Kabine ist da. Alle einsteigen!', 'Kabina je tady. Všichni nastoupit!'),
    # 1.3 the ride down
    ('zo_301', 'krgA', 'Partisanen am Hang! Feuer frei!', 'Partyzáni na svahu! Volná palba!'),
    ('zo_302', 'web', 'Die schießen auf die Kabine! Runter, runter!', 'Střílejí po kabině! K zemi, k zemi!'),
    ('zo_307', 'hof', 'Hält das Seil? Bitte, lass das Seil halten.', 'Vydrží to lano? Prosím, ať to lano vydrží…'),
    ('zo_303', 'krg', 'Talstation. Ausschwärmen! Sucht seine Spur!', 'Údolní stanice. Rozvinout se! Hledejte jeho stopu!'),
    ('zo_305', 'mul', 'Noch mehr von der Straße! Deckung!', 'Další od silnice! Kryt!'),
    ('zo_304', 'brn', 'Blut. Er ist verletzt. Er läuft nach Norden, in den Wald.', 'Krev. Je zraněný. Utíká na sever, do lesa.'),
    # 2.1 the forester's lodge
    ('zo_400', 'krg', 'Das Forsthaus liegt oben auf dem Hügel. Leise, Männer.', 'Hájovna je nahoře na kopci. Potichu, chlapi.'),
    ('zo_401', 'krg', 'Hier hat er sich mit den Partisanen getroffen. Durchsucht das Haus!', 'Tady se sešel s partyzány. Prohledejte dům!'),
    ('zo_402', 'brn', 'Eine Karte. Wolfsgrund ist rot eingekreist. Er will zur Fabrik!', 'Mapa. Wolfsgrund je zakroužkovaný červeně. Chce do továrny!'),
    ('zo_403', 'krg', 'Wolfsgrund, hier Krüger. Der Amerikaner kommt zu euch. Hört ihr mich? Wolfsgrund! Nichts.', 'Wolfsgrunde, tady Krüger. Ten Američan jde k vám. Slyšíte mě? Wolfsgrunde! … Nic.'),
    ('zo_404', 'web', 'Fallschirme! Über dem Wald!', 'Padáky! Nad lesem!'),
    ('zo_405', 'krg', 'Engländer. Jetzt holen sie ihn nach Hause.', 'Angličané. Teď si ho odvezou domů.'),
    # 2.2 Wolfsgrund
    ('zo_500', 'hof', 'Mein Gott. Die ganze Wache ist tot.', 'Můj bože. Celá stráž je mrtvá.'),
    ('zo_501', 'krg', 'Die Engländer halten die Rampe. Räumt sie! Und findet ihr Funkgerät!', 'Angličané drží rampu. Vyčistěte ji! A najděte jejich vysílačku!'),
    ('zo_506', 'krg', 'Die Rampe ist frei!', 'Rampa je čistá!'),
    ('zo_502', 'brn', 'Ihr Funkgerät ist hin. Jetzt kommt kein Flugzeug.', 'Jejich vysílačka je na kusy. Teď žádné letadlo nepřiletí.'),
    ('zo_503', 'krg', 'Der Notausgang aus dem Stollen, unter dem Felsen. Da kommt er raus.', 'Nouzový východ ze štoly, pod skálou. Tudy vyleze.'),
    ('zo_504', 'krgA', 'Der Berg! Runter! Alle runter!', 'Hora! K zemi! Všichni k zemi!'),
    # 2.3 below the burning mountain
    ('zo_601', 'brn', 'Krüger! Feldwebel!', 'Krügere! Pane Feldwebel!'),
    ('zo_602', 'krg', 'Lass mich, Brandt. Mein Bein. Geh. Hol ihn dir. Für Kessler und Vogt.', 'Nech mě, Brandte. Moje noha… Jdi. Dostaň ho. Za Kesslera a Vogta.'),
    ('zo_604', 'brn', 'Noch mehr Engländer. Die warten auf ihn.', 'Další Angličani. Čekají na něj.'),
    ('zo_603', 'brn', 'Jetzt gehörst du mir, Adler.', 'Teď jsi můj, Orle.'),
    # finale: the knife fight
    ('zo_f1', 'brn', 'Adler.', 'Orle.'),
    ('zo_f2', 'bj', 'Ty jsi ten ze strážnice. Měl jsem mířit líp.'),
    ('zo_f3', 'brn', 'Deine Waffe ist leer, Amerikaner. Meine auch.', 'Tvoje zbraň je prázdná, Američane. Moje taky.'),
    ('zo_f4', 'brn', 'Für Kessler. Für Vogt.', 'Za Kesslera. Za Vogta.'),
    ('zo_f5', 'bj', 'Tak pojď.'),
    ('zo_f6', 'bj', 'Pro Londýn.'),
]
LINES += LINES_ZO
# escaped prisoners and partisans shout in Czech (two voices, P and Q)
CZ_BARKS = {
    'sus': [('Co to bylo?', None), ('Je tam někdo?', None), ('Něco jsem slyšel.', None)],
    'alert': [('Němci! Tamhle jsou!', None), ('Palte!', None), ('Za Orla!', None), ('Pozor, skopčáci!', None)],
    'body': [('Zabili Jendu!', None), ('Tady leží jeden z našich!', None)],
    'lost': [('Nic. Asi vítr.', None), ('Už jsou pryč.', None)],
}
