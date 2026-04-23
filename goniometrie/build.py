import os
import subprocess
import sys
import argparse
from pathlib import Path

# Nastavení (shodné s Makefile)
DIRS = ["A_stupnova_mira", "B_obloukova_mira", "C_goniometricke_fce"]
GLOBAL_DEPS = ["config.py", "jednotkova_kruznice.py"]

# Mapování kvality na parametry Manimu
QUALITY_MAP = {
    "low": "-ql",     # 480p, 15fps
    "medium": "-qm",  # 720p, 30fps
    "high": "-qh"     # 1080p, 60fps
}

def get_class_name(file_path):
    """Získá název třídy (odřízne první 3 znaky '01_' a příponu)"""
    return file_path.stem[3:]

def build_video(file_path, quality_flag, light_mode="false"):
    """Renderuje jeden konkrétní soubor"""
    class_name = get_class_name(file_path)
    
    # Dynamická volba složky podle módu
    output_subdir = "slides_publish_LIGHT" if light_mode else "slides_publish_DARK"
    
    output_dir = file_path.parent / output_subdir
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{file_path.stem}.html"

    print(f"--- Rendering: {file_path.name} | quality: {quality_flag} | mode: ({'LIGHT' if light_mode else 'DARK'} mode) ---")

    # Nastavení proměnné prostředí pro config.py
    env = os.environ.copy()
    if light_mode:
        env["LIGHT_MODE"] = "true"

    # 1. Manim render
    manim_cmd = ["manim", quality_flag, str(file_path), class_name]
    subprocess.run(manim_cmd, check=True, env=env)

    # 2. Manim Slides konverze
    slides_cmd = ["manim-slides", "convert", class_name, str(output_file)]
    subprocess.run(slides_cmd, check=True)
    
    print(f"✅ Hotovo: {output_file}\n")

def main():
    parser = argparse.ArgumentParser(description="Build skript pro goniometrická videa.")
    parser.add_argument("file", nargs="?", help="Název souboru k renderu (např. 01_Stupne). Pokud chybí, renderuje vše.")
    parser.add_argument("-q", "--quality", choices=["low", "medium", "high"], default="low", help="Kvalita renderu (default: low)")
    parser.add_argument("--light", action="store_true", help="Renderovat ve světlém módu do slides_publish_LIGHT")
    parser.add_argument("--clean", action="store_true", help="Smaže pomocné soubory")
    
    args = parser.parse_args()
    quality_flag = QUALITY_MAP[args.quality]

    # Přepnutí do pracovní složky (pokud skript spouštíme z kořene)
    if Path("goniometrie").exists():
        os.chdir("goniometrie")

    if args.clean:
        # Jednoduchý úklid (volitelné)
        for d in ["media", "slides"]:
            if os.path.exists(d): 
                import shutil
                shutil.rmtree(d)
        print("Vyčištěno.")
        return

    # Sběr souborů k renderování
    targets = []
    if args.file:
        # Hledáme konkrétní soubor napříč složkami
        target_name = args.file if args.file.endswith(".py") else f"{args.file}.py"
        found = False
        for d in DIRS:
            potential_path = Path(d) / target_name
            if potential_path.exists():
                targets.append(potential_path)
                found = True
                break
        if not found:
            print(f"❌ Soubor {target_name} nebyl v podadresářích nalezen.")
            sys.exit(1)
    else:
        # Renderujeme vše
        for d in DIRS:
            targets.extend(list(Path(d).glob("[0-9][0-9]_*.py")))

    # Spuštění buildu pro vybrané cíle
    for t in targets:
        build_video(t, quality_flag, light_mode=args.light)

if __name__ == "__main__":
    main()