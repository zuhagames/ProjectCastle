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
    # transitions between missions (v1.4)
    ('bj_t1', 'bj', 'Z kobek jsem venku. Teď štáb SS – a plány operace Finsternis.'),
    ('bj_t2', 'bj', 'Plány mám. Zeman a jeho laboratoř jsou někde pod kaplí.'),
    ('bj_t3', 'bj', 'Podle mapy: lesní tábor, pak trať. Žádné světlo, žádný hluk.'),
    ('bj_t4', 'bj', 'Odtud jede zvláštní vlak. Bez čísla a bez cíle v papírech.'),
    ('bj_t5', 'bj', 'Jsem uvnitř. Teď dopředu, vagon po vagonu – až k lokomotivě.'),
    ('bj_t6', 'bj', 'Sto metrů pod horou. Tady stavějí Finsternis.'),
    ('bj_t7', 'bj', 'Doktore Zemane. Konečně se poznáme.'),
]
BARKS = {
    'sus': [('Was war das?', 'surprised'), ('Hallo? Ist da jemand?', 'surprised'), ('Hm? Wer ist da?', 'neutral'), ('Da hat sich was bewegt.', 'neutral')],
    'alert': [('Alarm!', 'angry'), ('Da ist er!', 'angry'), ('Halt! Stehen bleiben!', 'angry'), ('Feind gesichtet!', 'angry')],
    'body': [('Mein Gott, ein Toter!', 'surprised'), ('Hier liegt einer! Alarm!', 'angry')],
    'lost': [('Nichts. Muss der Wind gewesen sein.', 'neutral'), ('Nur eine Ratte.', 'neutral'), ('Ich sehe niemanden.', 'neutral')],
}
