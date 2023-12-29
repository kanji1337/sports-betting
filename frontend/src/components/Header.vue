<template>
	<header class="flex justify-between border-b border-slate-300 px-8 py-8">
		<div class="flex items-center gap-4">
			<img src="/logo.png" alt="Logo" class="w-12" />
			<div>
				<h2 class="text-xl font-bold uppercase">Букмейкерка322</h2>
				<p class="text-slate-500">Ставьте, выйграйте, забирайте</p>
			</div>
		</div>

		<ul class="flex items-center gap-10">
			<li
				class="flex items-center gap-3 text-gray-500 hover:text-black cursor-pointer"
			>
				<img class="w-7" src="/calendar.svg" alt="Calendar" />
				<span>Календарь событий</span>
			</li>
			<li
				class="flex items-center gap-3 text-gray-500 hover:text-black cursor-pointer"
			>
				<img class="w-8" src="/balance.png" alt="Cart" />
				<span>1200 руб.</span>
			</li>
			<li
				class="flex items-center gap-3 text-gray-500 hover:text-black cursor-pointer"
			>
				<img class="w-6" src="/bets.png" alt="Cart" />
				<span>Ваши ставки</span>
			</li>
			<li
				class="flex items-center gap-3 text-gray-500 hover:text-black cursor-pointer"
			>
				<img src="/profile.svg" alt="Profile" />
				<span>Профиль</span>
			</li>
		</ul>
	</header>
</template>
