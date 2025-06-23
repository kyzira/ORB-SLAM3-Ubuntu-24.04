import os
import sys
import subprocess
import csv

def extract_frames_and_timestamps(video_path):
    # Verzeichnispfad für die Bilder
    image_dir = "dataset/mav0/cam0/data"
    csv_path = os.path.join(os.path.dirname(image_dir), "data.csv")
    timestamps_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(image_dir))), "timestamps.txt")

    # Ordner erstellen falls nicht vorhanden
    os.makedirs(image_dir, exist_ok=True)

    # ffmpeg Befehl zum Extrahieren der Frames
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", video_path,
        "-qscale:v", "2",
        "-vsync", "0",
        "-start_number", "0",
        os.path.join(image_dir, "%06d.png")
    ]
    print(f"Starte ffmpeg für {video_path}...")
    subprocess.run(ffmpeg_cmd, check=True)
    print("Frames extrahiert.")

    # ffprobe Befehl zum Auslesen der Timestamps (in Sekunden)
    ffprobe_cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "frame=best_effort_timestamp_time",
        "-of", "csv=p=0",
        video_path
    ]
    result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    lines = result.stdout.strip().split("\n")

    # Timestamps in Nanosekunden umwandeln
    timestamps = [int(float(t.strip().rstrip(',')) * 1e9) for t in lines if t.strip()]

    # Liste aller extrahierten Bilddateien sortieren
    image_files = sorted(f for f in os.listdir(image_dir) if f.endswith(".png"))

    if len(timestamps) != len(image_files):
        print(f"❌ Fehler: Anzahl Frames ({len(image_files)}) stimmt nicht mit Anzahl Timestamps ({len(timestamps)}) überein.")
        sys.exit(1)

    # CSV mit Timestamp und Filename schreiben
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["#timestamp [ns]", "filename"])
        for fname, ts in zip(image_files, timestamps):
            writer.writerow([ts, fname])
    print(f"✅ {len(timestamps)} Timestamps in {csv_path} geschrieben.")

    # timestamps.txt mit Bildnamen ohne Endung schreiben
    with open(timestamps_path, "w", newline="") as f:
        for fname in image_files:
            name_wo_ext = os.path.splitext(fname)[0]
            f.write(name_wo_ext + "\n")
    print(f"✅ Bildnamen ohne Endung in {timestamps_path} geschrieben.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python script.py <Pfad_zum_Video>")
        sys.exit(1)

    video_path = sys.argv[1]
    if not os.path.isfile(video_path):
        print(f"Die angegebene Datei existiert nicht: {video_path}")
        sys.exit(1)

    extract_frames_and_timestamps(video_path)
