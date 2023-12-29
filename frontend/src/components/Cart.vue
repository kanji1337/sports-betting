<script setup>
defineProps({
	title1: String,
	title2: String,
	imageUrl1: String,
	imageUrl2: String,
	time: Number,
	koef1: Number,
	koef2: Number,
	isFavorite: Boolean,
	isAdded: Boolean,
	onClickFav: Function,
	onClickAdd: Function,
});
</script>

<template>
	<div>
		<div class="flex items-center px-10 py-5">
			<img
				@click="onClickFav"
				class="w-5 hover: cursor-pointer"
				:src="isFavorite ? '/like-2.png' : '/like-1.png'"
				alt="like1"
			/>
			<div class="grid place-content-around">
				<span class="text-xs">{{ title1 }}</span>
				<img class="px-10 py-2" :src="imageUrl1" alt="Image1" />
			</div>
			<div class="grid grid-cols-1 grid-rows-2 items-center">
				<b>Против</b>
				<div>
					<span class="text-xs">Время: </span>
					<b class="text-xs">{{ time }}</b>
				</div>
			</div>
			<div class="flex flex-col">
				<span class="text-xs px-12">{{ title2 }}</span>
				<img
					class="px-10 py-2 object-scale-down"
					:src="imageUrl2"
					alt="Image2"
				/>
			</div>
			<b>Сделать ставку:</b>
			<div>
				<ul class="max-w-md dark:text-black-400 px-5 text-xs space-y-3">
					<li
						class="border-solid border-1 translate hover:bg-gray-400 cursor-pointer hover:-translate-y-1"
					>
						x{{ koef1 }} Победа: {{ title1 }}
					</li>
					<li
						class="border-solid border-1 translate hover:bg-gray-400 cursor-pointer hover:-translate-y-1"
					>
						x{{ koef2 }} Победа: {{ title2 }}
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
