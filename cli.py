#!/usr/bin/env python3
"""
FluxBatchCost — Commercial Image & Video Generation Arbitrage Calculator — Command-Line Cost Calculator
Live Web Calculator: https://sectoroneventures.github.io/flux-batch-cost/
"""
import argparse

PROVIDERS = [
  {
    "name": "Vast.ai Rented RTX 4090 (1-Click ComfyUI / Forge)",
    "cost_per_unit": 0.58,
    "min_monthly": 0.35,
    "speed_note": "~600 images/hr on RTX 4090 ($0.35/hr) or RTX 3090 ($0.19/hr)",
    "cta_label": "Boot 1-Click Flux Studio \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d",
    "highlight": true
  },
  {
    "name": "Per-Image Cloud Inference API ($0.04/image)",
    "cost_per_unit": 40.0,
    "min_monthly": 0.0,
    "speed_note": "$400 per 10,000 images with rate limits",
    "cta_label": "Rent Raw GPU & Save 98% \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467",
    "highlight": false
  }
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Compare per-image API pricing ($0.04-$0.08/image) against running Flux.1 Dev and Wan2.1 on a rented $0.19-$0.35/hr GPU.")
    parser.add_argument("--volume", type=float, default=10, help="Monthly Flux.1 Images to Generate (in Thousands)")
    args = parser.parse_args()
    print(f"=== {args.volume:g} k images/mo Cost Comparison ===")
    for p in PROVIDERS:
        cost = max(float(p["min_monthly"]), args.volume * float(p["cost_per_unit"]))
        print(f"* {p['name']}: ${cost:,.2f}/mo ({p['speed_note']})")
        print(f"  -> {p['cta_url']}")
    print(f"\nInteractive web calculator: https://sectoroneventures.github.io/flux-batch-cost/")

if __name__ == "__main__":
    main()
