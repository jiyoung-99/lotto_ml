<template>
    <div>
        <b-navbar toggleable="lg" type="dark"  class="navbar">
            <b-navbar-nav class="ml-auto">
            <b-navbar-brand :to="{ path: '/' }" >로또당첨번호예측</b-navbar-brand>
            <b-navbar-brand :to="{ path: '/lotto' }" >로또현황</b-navbar-brand>
            <b-navbar-brand :to="{ path: '/support' }" >개발자문의</b-navbar-brand>
            </b-navbar-nav>
            <!-- <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item href="#">Link</b-nav-item>
                <b-nav-item href="#" disabled>Disabled</b-nav-item>
            </b-navbar-nav> -->


            <!-- Right aligned nav items -->
            <!-- <b-navbar-nav class="ml-auto">
                <b-nav-form>
                <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>

                <b-nav-item-dropdown text="Lang" right>
                <b-dropdown-item href="#">EN</b-dropdown-item>
                <b-dropdown-item href="#">ES</b-dropdown-item>
                <b-dropdown-item href="#">RU</b-dropdown-item>
                <b-dropdown-item href="#">FA</b-dropdown-item>
                </b-nav-item-dropdown>

                <b-nav-item-dropdown right> -->
                <!-- Using 'button-content' slot -->
                <!-- <template #button-content>
                    <em>User</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav> 
            </b-collapse>-->
        

        </b-navbar>
    </div>
</template>
<style>
.navbar{
    /* position: relative; */
    font-family: sans-serif;
    background-image: linear-gradient(100deg, #641cda, #280ad1);
    min-height: 5rem;
    box-shadow: 0px 1px 20px gray;
}
</style>