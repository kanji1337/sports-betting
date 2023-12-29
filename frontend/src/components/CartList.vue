<script setup>
import Cart from "./Cart.vue";

defineProps({
	items: Array,
});

const onClickFav = () => {
	alert(1);
};
</script>

<template>
	<div class="Carts m-5 divide-y divide-slate-700 rounded-3xl">
		<div>
			<Cart
				v-for="item in items"
				:key="item.id"
				:is-favorite="false"
				:image-url1="item.imageUrl1"
				:image-url2="item.imageUrl2"
				:time="item.time"
				:title1="item.title1"
				:title2="item.title2"
				:koef1="item.koef1"
				:koef2="item.koef2"
				:on-click-fav="onClickFav"
			/>
		</div>
	</div>
</template>
