<script setup>
import { ref, onMounted } from "vue";
import Header from "./components/Header.vue";
import CartList from "./components/CartList.vue";
//import Bets from "./components/Bets.vue";
const items = ref([]);

onMounted(async () => {
	try {
		const response = await fetch("http://localhost:8000/api/items/"); // Замените на адрес вашего Django API
		const data = await response.json();
		items.value = data.items;
	} catch (error) {
		console.error("Error fetching data:", error);
	}
});
</script>

<template>
	<div class="w-4/5 m-auto bg-white h-screen rounded-xl shadow-xl mt-7">
		<Header />
		<h4 class="text-3xl font-bold mt-5 ml-10">Футбол ЧМ 2024</h4>
		<CartList :items="items" />
	</div>
</template>
