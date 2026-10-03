def generate_summary(lsb_results, chi_results, dct_results, stats):

    observations = []

    lsb_imbalance = lsb_results["imbalance"]

    if lsb_imbalance < 0.02:
        observations.append(
            f"The LSB distribution is relatively balanced, "
            f"with an imbalance of {lsb_imbalance:.2%}."
        )
    else:
        observations.append(
            f"The LSB distribution shows a noticeable imbalance "
            f"of {lsb_imbalance:.2%}."
        )

    significant_channels = []

    for channel, result in chi_results.items():
        if result["p_value"] < 0.05:
            significant_channels.append(channel)

    if significant_channels:
        observations.append(
            "Chi-square analysis detected statistically unusual "
            "distributions in the "
            + ", ".join(significant_channels)
            + " channel(s)."
        )
    else:
        observations.append(
            "Chi-square analysis did not detect statistically "
            "unusual distributions at the 5% significance level."
        )

    observations.append(
        f"DCT analysis produced a mean coefficient magnitude of "
        f"{dct_results['mean_dct']:.2f} with "
        f"{dct_results['high_frequency_ratio']:.2%} "
        f"of energy in higher-frequency coefficients."
    )

    return {
        "status": "Analysis Completed",
        "message": " ".join(observations),
        "disclaimer": (
            "These indicators are statistical observations only "
            "and do not independently confirm the presence of "
            "hidden information."
        )
    }