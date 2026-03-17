process clean_data {

    tag "clean metabolite table"

    publishDir "results", mode: 'copy'
    conda "environment.yml"

    input:
    path data

    output:
    path "clean.csv"

    script:
    """
    clean_data.py $data clean.csv
    """
}

process normalize_data {

    tag "normalise intensities"

    publishDir "results", mode: 'copy'
    conda "environment.yml"

    input:
    path data

    output:
    path "normalized.csv"

    script:
    """
    normalize_data.py $data normalized.csv
    """
}

process pca_analysis {

    tag "PCA analysis"

    publishDir "results", mode: 'copy'
    conda "environment.yml"

    input:
    path data

    output:
    path "pca.png"

    script:
    """
    pca_analysis.py $data pca.png
    """
}

process differential_analysis {

    tag "differential metabolites"

    publishDir "results", mode: 'copy'
    conda "environment.yml"

    input:
    path data

    output:
    path "differential_metabolites.csv"

    script:
    """
    differential_analysis.py $data differential_metabolites.csv
    """
}

workflow {

    raw = channel.fromPath("data/metabolomics.tsv")

    cleaned = clean_data(raw)

    normalized = normalize_data(cleaned)

    pca_analysis(normalized)

    differential_analysis(normalized)
}