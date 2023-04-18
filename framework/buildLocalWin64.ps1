[CmdletBinding()]
param (
    [Parameter()]
    [switch]
    $Server,

    [Parameter()]
    [switch]
    $Client,

    [Parameter()]
    [string]
    $ExportClient,

    [Parameter()]
    [string]
    $ExportServer,

    [Parameter()]
    [switch]
    $CleanLocal
)


if ($CleanLocal -and (Test-Path .\out)) {
    Remove-Item .\out -Recurse
}


if ($ExportClient) {
    java -jar .\tools\openapi-generator-cli.jar generate `
            --generator-name python `
            --template-dir .\templates\python `
            --input-spec openapi.yaml `
            --output $ExportClient
}

if ($ExportServer) {
    java -jar .\tools\openapi-generator-cli.jar generate `
                --generator-name python-flask `
                --template-dir .\templates\pythonFlask `
                --input-spec openapi.yaml `
                --output $ExportServer
}

if ($Client) {
java -jar .\tools\openapi-generator-cli.jar generate `
            --generator-name python `
            --template-dir .\templates\python `
            --input-spec openapi.yaml `
            --output .\out\pythonClient `
            --global-property skipFormModel=false
}

if ($Server) {
java -jar .\tools\openapi-generator-cli.jar generate `
            --generator-name python-flask `
            --template-dir .\templates\pythonFlask `
            --input-spec openapi.yaml `
            --output .\out\pythonFlaskServer `
            --global-property skipFormModel=false
}