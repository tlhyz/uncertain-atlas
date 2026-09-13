#!/usr/bin/env python3
"""Run Tech state-machine experiment (wrapper)."""

from qtb.dual.run import main

if __name__ == "__main__":
    raise SystemExit(main(["-c", "configs/dual_engine_perp.yaml"]))
