# Vizualizace goniometrie (Manim Slides)

Tento repozitář obsahuje zdrojové kódy k 20 interaktivním videím (prezentacím) vytvořeným v knihovně **Manim** a **Manim Slides**. Projekt vznikl jako součást diplomové práce v oboru Učitelství matematiky (MFF UK 2026) a je navržen tak, aby jej učitelé mohli snadno upravovat nebo používat ve výuce.

## Požadavky na systém

Před spuštěním je nutné mít v systému nainstalovány tyto komponenty:

- Python 3.12+
- LaTeX (distribuce TeX Live nebo MiKTex -- nutné pro renderování matematických symbolů)
- editor pro jazyk Python (doporučuji Visual Studio Code)

## Instalace

Zde je popsáno, jak lze vytvořit kopii projektu a samostatně na ní pracovat. Můžete pak upravovat hotová videa nebo tvořit nová.

### 1. Klonování (stažení) projektu

Projekt je sdílený na platformě GitHub. Máte možnost vytvořit si na svém PC vlastní kopii tohoto projektu, kterou můžete po svém upravovat. Stačí otevřít terminál (u Windows PowerShell), pomocí `cd` se přemístit do složky, ve které chcete mít projekt, a následně zadat následující příkazy.

```bash
git clone https://github.com/grow-tea/manimations.git
cd manimations
```

### 2. Vytvoření a aktivace virtuálního prostředí

Projekt využívá virtuální prostředí Pythonu (`.venv`). To slouží k tomu, aby se knihovny projektu (Manim, Manim Slides) nepletly s ostatními programy ve Vašem počítači. Pro vytvoření virtuálního prostředí zadejte následující.


Pro Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Pro Windows:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instalace knihoven

Knihovny jsou již pohodlně sepsány v souboru `requirements.txt`, stačí pouze stáhnout.

```bash
pip install -r requirements.txt
```

### 4. Opětovné spuštění (návrat k práci)

Po opětovném otevření projeku je nutné znova aktivovat virtuální prostředí `.venv`. Do terminálu (třeba přímo ve VS Code) stačí před začátkem práce zadat

Pro Linux/MacOS: `source .venv/bin/activate`

Pro Windows: `.\.venv\Scripts\activate`

## Struktura projektu

Hlavní logika se nachází ve složce `goniometrie/`. V ní se nachází následující soubory:

- `Jednotkova_kruznice.py` je základní třída, ze které ostatní soubory čerpají grafické prvky
- `config.py` řídí globální nastavení vzhledu
- `A_stupnova_mira/`, `B_obloukova_mira/` a `C_goniometricke_fce/` jsou složky obsahující samostatné `.py` soubory pro videa
- v těchto složkách jsou dále k nalezení `vysledky_LIGHT` a `vysledky_DARK`, což jsou výsledná videa (resp. prezentace) ve formátu `.html`

Další soubory jsou již pouze technického rázu. Pro úpravu videí stačí pracovat s vyjmenovanými soubory a složkami.

## Jak vyrenderovat videa

Videa lze renderovat přímo voláním příkazů `manim` a `manim-slides` pro jednotlivá videa. Pro pohodlí uživatele však v projektu je soubor `builder.py`, díky němuž lze pohodlně renderovat i všechna videa najednou.

Ujistěte se, že jste ve složce `goniometrie/`, aby bylo možné k souboru `builder.py` přistoupit. Soubor se pak ovládá následovně:

- pro renderování všech videí jednoho po druhém stačí zavolat `python build.py`
- vyrenderovat všechny videa ve světlém módu `python build.py --light`
- ze zdrojového souboru `01_Zlomky_na_stupne.py` vyrenderujeme video příkazem `python build.py 01_Zlomky_na_stupne`
- předchozí, ale ve světlém módu `python build.py 01_Zlomky_na_stupne --light`
- zobrazení nápovědy `python build.py --help`
- `python build.py -q medium` videa budou renderována v kvalitě 720p (namísto defaultních 480p)
- `python build.py 01_Zlomky_na_stupne -q high` první video bude vyrenderované v kvatitě 1080p

Upozorňuji, že (v závislosti na výkonu vašeho PC) může renderování všech 20 videí trvat desítky minut, a to i při nízké kvalitě! Render jednoho videa bude typicky trvat okolo minuty.

Výstupem je `.html` soubor, který je možné otevřít v libovolném webovém prohlížeči nebo též umístit na vlastní webové stránky. K tomuto souboru je zhotovena též pomocná složka `..._assets`, která musí umístěna ve stejném místě co samotný soubor, jinak nebude možné video zprovoznit.

## Jak ovládat videa

Máme-li hotový soubor `.html`, stačí jej otevřít v libovolném webovém prohlížeči (Firefox, Chrome). Ovládání vizualizace je následující:

- `Šipka vpravo` další úsek videa
- `Šipka vlevo` předchozí úsek videa
- `mezerník` spuštění nebo zastavení videa; případně zopakování poslední animace
- `F` video na celou obrazovku
- `R` přehraj znovu
- `H` skryj kurzor myši
- `V` zpětný chod (reverse)
- `Q` ukončení (quit)

## Jak tvořit další videa

S doposud popsaným návodem můžete být schopni upravovat, renderovat a prohlížet již vytvořená videa ve složce `goniometrie/`, a to bez úpravy souboru `builder.py`. Pokud chcete tvořit další videa (i mimo oblast goniometrie), bude nutné soubor `builder.py` příslušně upravit. Původně je schopen renderovat videa začínající dvěma číslicemi a podtržítkem, vše lze změnit dle Vaší preference.

Videa s jednotkovou kružnicí by mělo být díky pomocné třídě v `jednotkova_kruznice.py` jednodušší tvořit. Pokud máte zájem opustit oblast goniometrie, doporučuji v podobném duchu tvořit pomocné třídy pro Vaše videa.