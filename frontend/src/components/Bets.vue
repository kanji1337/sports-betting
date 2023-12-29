<script setup>
import BetsHeader from "./BetsHeader.vue";
import CartItemList from "./CartItemList.vue";
</script>

<template>
	<div>
		<div
			class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-70"
		></div>
		<div class="bg-white w-96 h-full fixed right-0 top-0 z-20 p-8">
			<BetsHeader />
			<CartItemList />

			<div class="flex gap-2">
				<span>Сумма ставки: </span>
				<div class="flex-1 border-b border-dashed"></div>
				<b>12900</b>
			</div>

			<button
				disabled=""
				class="transition mt-2 bg-lime-500 w-full cursor-pointer disabled:bg-slate-400 rounded-xl py-5 text-white hover:bg-lime-600 active:bg=lime-700"
			>
				Сделать ставку
			</button>
		</div>
	</div>
</template>
