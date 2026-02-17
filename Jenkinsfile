@Library('datenshi-ci') _

datenshiPipeline(
    service      : 'avatarserver',
    // Only build on develop; Jenkins job should be configured accordingly,
    // but this is a cheap extra guard.
    runTests     : false,
    runDeploy    : false,
    // Image name (without registry host); registry URL is stored in Jenkins
    // as a secret text credential "datenshi-registry-url".
    image        : 'datenshi/avatarserver',
    tag          : env.GIT_COMMIT ?: env.BUILD_NUMBER,
    credentialsId: 'datenshi-registry'
)

