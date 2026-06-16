# ReconForge

<p align="center">

Automated Reconnaissance Framework

</p>


## Overview

ReconForge is a modular CLI based reconnaissance framework designed to automate the reconnaissance workflow.

It performs:

- Environment detection
- Tool verification
- Passive reconnaissance
- Active reconnaissance
- Technology fingerprinting
- Vulnerability discovery
- Risk analysis
- HTML reporting


## Features

### Recon Engine

- Modular architecture
- Session based scans
- JSON evidence storage
- Raw command outputs


### Recon Modules

- Subdomain enumeration
- HTTP discovery
- Port scanning
- Technology detection
- Nuclei vulnerability scanning


### Reporting

- Professional HTML reports
- Risk scoring
- Evidence tracking
- Timestamped results


## Installation


Clone repository:


```bash
git clone https://github.com/muhammadtalha1322/ReconForge.git

cd ReconForge
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Check environment:

```bash
python3 reconforge.py check
```

## Usage

Start scan:

```bash
python3 reconforge.py scan -t target.com
```

Generate report:

```bash
python3 reconforge.py report \
-i output/sessions/session/results.json
```

## Project Structure

```
ReconForge

core/
    engine
    runner
    rules

modules/

    passive
    active
    fingerprint
    web


reports/

output/

scripts/

```

## Legal

Use only against systems you own or have explicit authorization to test.

## License

MIT
