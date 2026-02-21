@Library('datenshi-ci') _

datenshiPipeline(
    service       : 'avatarserver',
    runTests      : false,
    runDeploy     : true,
    image         : 'datenshi/avatarserver',
    tag           : env.BUILD_NUMBER,
    credentialsId : 'datenshi-registry',
)

