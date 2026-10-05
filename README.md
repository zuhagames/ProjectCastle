# Castle Grimhold

**Operation Iron Wolf · 1943** – 3D FPS z druhé světové války běžící přímo v prohlížeči, postavený na [three.js](https://threejs.org/) (r160).

Proplížíš se a probojuješ hradem Grimhold přes tři mise:

1. **Mise 1 · Kobky**
2. **Mise 2 · Velitelství**
3. **Mise 3 · Krypta**

## Spuštění

Hra je jeden HTML soubor, ale kvůli načítání assetů ji spusť přes lokální server (ne přes `file://`):

```bash
python -m http.server 8765 --bind 127.0.0.1
```

Pak otevři <http://127.0.0.1:8765/castle_grimhold.html>.

Three.js a modely postav se načítají z CDN (jsDelivr), takže je potřeba připojení k internetu. Webové textury jsou volitelné – když nejsou dostupné, hra si textury vygeneruje procedurálně.

## Ovládání

| Klávesa | Akce |
| --- | --- |
| `WASD` | pohyb |
| `Space` | skok |
| `LMB` | střelba |
| `RMB` | zaměřovač |
| `R` | přebít |
| `F` | použít / dveře |
| `Q` / `E` | vyklonit se |
| `Shift` | sprint |
| `C` | přikrčit / plížit |
| `1`–`6` / kolečko | výběr zbraně |
| `Tab` | úkoly mise |
| `M` | zvuk on/off |
| `Esc` | pauza |

## Zbraně

Lee-Enfield No.4, revolver, Sten, plamenomet, mačeta a granát (Stielhandgranate).

## Struktura projektu

```
castle_grimhold.html   # celá hra (HTML + JS)
assets/
  models.js            # zbraně (FBX) zabalené do JS
  characters.js        # postavy zabalené do JS
  models/              # zdrojové modely (.fbx, .glb)
  CREDITS.txt          # autoři a licence assetů
```

## Credits

3D modely zbraní jsou CC0 z [OpenGameArt.org](https://opengameart.org/) (Lucian Pavel, ege, elmerenges), postavy pocházejí z příkladů three.js (MIT / Mixamo). Podrobnosti v [assets/CREDITS.txt](assets/CREDITS.txt).
