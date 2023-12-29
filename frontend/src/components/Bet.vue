<template>
	<div>
		<div class="border border-slate-200 p-1 rounded-xl mb-4">
			<p>Россия против Куба</p>
			<div class="flex mt-2 justify-between ml-10 mr-10">
				<span>Выбор: </span>
				<b class="cursor-pointer">Россия</b>
				<b class="cursor-pointer">Куба</b>
			</div>
			<div class="flex justify-between mt-2">
				<b>Введите сумму ставки</b>
				<input class="w-20" />
				<img
					class="cursor-pointer opacity-40 hover:opacity-100"
					src="/close.svg"
				/>
			</div>
			<div class="flex">
				<b>Возможный выйгрыш</b>
				<span></span>
			</div>
			<div class="flex justify-center">
				<button>Поставить</button>
			</div>
		</div>
	</div>
</template>
