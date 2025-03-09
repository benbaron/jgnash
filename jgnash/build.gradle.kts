plugins {
    id("com.github.ben-manes.versions")
	id("java")
    id("eclipse")
}
    

allprojects {
    repositories {
        mavenCentral()
        jcenter()
        mavenLocal()
    }

    apply(plugin = "java")
}

subprojects {
    group = "jgnash"
    version = "3.6.0"
}



