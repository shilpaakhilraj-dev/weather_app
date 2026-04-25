import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Weather CLI App")

    parser.add_argument("--city", type=str, help="City name")
    parser.add_argument("--lat", type=float, help="Latitude")
    parser.add_argument("--lon", type=float, help="Longitude")
    parser.add_argument("--units", choices=["metric", "imperial"], default="metric")

    return parser.parse_args()