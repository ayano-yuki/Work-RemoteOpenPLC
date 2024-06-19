<template>
  <TopicPath id="topicpath"></TopicPath>
  <div id="str-title"> Remote OpenPLC</div>
  
  <div id="contens-center">
      <HomeButton name="Setting" path='../../public/svg/setting.svg' next="setting"></HomeButton>
      <HomeButton name="Run OpenPLC" path='../../public/svg/running.svg' next="running"></HomeButton>
  </div>
</template>

<script setup>
import HomeButton from '@/components/button/HomeButton.vue';
import TopicPath from '@/components/TopicPath.vue';

</script>

<style scoped>
#contens-center {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>