# FluxBatchCost — Commercial Image & Video Generation Arbitrage Calculator

👉 **Live Interactive Calculator:** **[https://sectoroneventures.github.io/flux-batch-cost/](https://sectoroneventures.github.io/flux-batch-cost/)**

Per-image APIs charge $40-$80 per 1,000 Flux.1 images, whereas renting an RTX 4090 ($0.35/hr) on Vast.ai generates ~600 Flux.1 Dev images per hour (~$0.58 per 1,000 images — a 98.5% cost savings).

---

## Quick Comparison Table

| Stack / Provider | Notes | Direct Link |
| :--- | :--- | :--- |
| **Vast.ai Rented RTX 4090 (1-Click ComfyUI / Forge)** | ~600 images/hr on RTX 4090 ($0.35/hr) or RTX 3090 ($0.19/hr) | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d)** |
| **Per-Image Cloud Inference API ($0.04/image)** | $400 per 10,000 images with rate limits | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467)** |

---

## Run From Your Terminal (`cli.py`)

```bash
python3 cli.py --volume 10
```

## Related Developer Cost Calculators
* **[GPU Memory & Hourly Price Calculator](https://sectoroneventures.github.io/infrabench/)**
* **[Headless Browser & Scraping API Benchmark](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)**
* **[Docker VPS vs. Cloud Scraper TCO Estimator](https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html)**
