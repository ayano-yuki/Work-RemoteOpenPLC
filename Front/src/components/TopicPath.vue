<template>
    <div class="breadcrumb-container">
        <template v-for="(segment, index) in topic">
            <router-link v-if="index < topic.length - 1" :key="index" :to="getBreadcrumbPath(segment)"
                class="breadcrumb-link">
                {{ segment }}
            </router-link>
            <span v-else class="breadcrumb-segment">{{ segment }}</span>
            <span v-if="index < topic.length - 1" class="separator"> > </span>
        </template>
    </div>

    <!-- <div>{{ this.$route }}</div> -->
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue';


const props = defineProps(['path'])
const router = useRouter()
const topic = ref(["Home"])
const pathSegments = ref()

onMounted(() => {
    const currentPath = router.currentRoute.value.path
    pathSegments.value = currentPath.split('/').filter(segment => segment !== '')

    topic.value.push(...pathSegments.value)
});

const getBreadcrumbPath = (segment) => {
    if (segment == "Home") {
        return "/"
    }

    else {
        return segment
    }
}
</script>

<style scoped>
.breadcrumb-container {
    display: flex;
}

.breadcrumb-link {
    margin-right: 5px;
    text-decoration: underline;
    color: var(--color-close-link);
}

.breadcrumb-segment {
    margin-right: 5px;
}

.separator {
    margin: 0 5px;
    color: var(--color-open-link);
}
</style>