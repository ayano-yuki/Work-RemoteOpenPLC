<template>
    <div class="buttonIconText" @click="experiment.clear_result()">
        <span class="buttonIconText_icon">
            <img width="32" height="32" viewBox="0 0 24 24" :src="'../../../public/svg/clear.svg'">
        </span>
        <span class="buttonIconText_text">Clear</span>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { controller_experiment } from '@/stores/counter';

const experiment = controller_experiment();
</script>

<style scoped>
.buttonIconText {
    display: flex;
    gap: 8px;
    align-items: center;
    width: 100%;
    max-width: 70em;
    height: 64px;
    padding: 8px 40px 8px 8px;
    font-family: sans-serif;
    font-size: 16px;
    color: var(--color-button-text);
    text-align: center;
    overflow-wrap: anywhere;
    background-color: var(--color-button-background);
    border-radius: 32px;
    margin-bottom: 8%;
}

.buttonIconText__reverse {
    flex-direction: row-reverse;
    padding: 8px 8px 8px 40px;
}

.buttonIconText_icon {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: center;
    width: 48px;
    aspect-ratio: 1;
    padding: 4px;
    overflow: hidden;
    background-color: var(--color-button-icon);
    border-radius: 50%;
}

.buttonIconText_text {
    flex-shrink: 1;
    font-weight: bolder;
    font-size: larger;
    width: 100%;
    user-select: none;
}

@media (any-hover: hover) {
    .buttonIconText {
        transition: background-color 0.2s;
    }

    .buttonIconText_icon_item {
        transition: background-color 0.2s;
    }

    .buttonIconText:hover {
        background-color: var(--color-button-hover);
    }
}
</style>