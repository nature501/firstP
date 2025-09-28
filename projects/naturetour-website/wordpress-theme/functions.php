<?php
/**
 * NatureTour Pro WordPress Theme Functions
 * 自然國際旅行社專用主題功能
 *
 * @package NatureTour
 * @version 1.0.0
 */

// 防止直接訪問
if (!defined('ABSPATH')) {
    exit;
}

// 主題版本常數
define('NATURETOUR_VERSION', '1.0.0');
define('NATURETOUR_THEME_DIR', get_template_directory());
define('NATURETOUR_THEME_URI', get_template_directory_uri());

/**
 * ==========================================================================
 * 主題基礎設置
 * ==========================================================================
 */

function naturetour_setup() {
    // 啟用主題支援功能
    add_theme_support('post-thumbnails');
    add_theme_support('title-tag');
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'script',
        'style'
    ));

    // 自訂圖片尺寸
    add_image_size('destination-card', 400, 250, true);
    add_image_size('blog-featured', 800, 400, true);
    add_image_size('testimonial-avatar', 80, 80, true);

    // 註冊導航選單
    register_nav_menus(array(
        'main-menu' => '主導航選單',
        'footer-menu' => '頁腳選單',
        'service-menu' => '服務選單'
    ));

    // 語言支援
    load_theme_textdomain('naturetour', NATURETOUR_THEME_DIR . '/languages');
}
add_action('after_setup_theme', 'naturetour_setup');

/**
 * ==========================================================================
 * 資源載入
 * ==========================================================================
 */

function naturetour_scripts_styles() {
    // 主要樣式表
    wp_enqueue_style(
        'naturetour-style',
        get_stylesheet_uri(),
        array(),
        NATURETOUR_VERSION
    );

    // Google Fonts
    wp_enqueue_style(
        'naturetour-fonts',
        'https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@300;400;500;700&display=swap',
        array(),
        null
    );

    // Font Awesome
    wp_enqueue_style(
        'font-awesome',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css',
        array(),
        '6.0.0'
    );

    // 主要JavaScript
    wp_enqueue_script(
        'naturetour-main',
        NATURETOUR_THEME_URI . '/assets/js/main.js',
        array('jquery'),
        NATURETOUR_VERSION,
        true
    );

    // Ajax支援
    wp_localize_script('naturetour-main', 'naturetour_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('naturetour_nonce')
    ));
}
add_action('wp_enqueue_scripts', 'naturetour_scripts_styles');

/**
 * ==========================================================================
 * 小工具區域註冊
 * ==========================================================================
 */

function naturetour_widgets_init() {
    // 主側邊欄
    register_sidebar(array(
        'name' => '主側邊欄',
        'id' => 'main-sidebar',
        'description' => '主要側邊欄區域',
        'before_widget' => '<div class="widget %2$s">',
        'after_widget' => '</div>',
        'before_title' => '<h3 class="widget-title">',
        'after_title' => '</h3>'
    ));

    // 頁腳小工具區域
    for ($i = 1; $i <= 4; $i++) {
        register_sidebar(array(
            'name' => "頁腳區域 $i",
            'id' => "footer-$i",
            'description' => "頁腳第 $i 欄位",
            'before_widget' => '<div class="footer-widget %2$s">',
            'after_widget' => '</div>',
            'before_title' => '<h4 class="footer-widget-title">',
            'after_title' => '</h4>'
        ));
    }
}
add_action('widgets_init', 'naturetour_widgets_init');

/**
 * ==========================================================================
 * 自訂文章類型
 * ==========================================================================
 */

function naturetour_custom_post_types() {
    // 旅遊目的地文章類型
    register_post_type('destination', array(
        'labels' => array(
            'name' => '旅遊目的地',
            'singular_name' => '目的地',
            'add_new' => '新增目的地',
            'add_new_item' => '新增旅遊目的地',
            'edit_item' => '編輯目的地',
            'new_item' => '新目的地',
            'view_item' => '查看目的地',
            'search_items' => '搜尋目的地',
            'not_found' => '找不到目的地',
            'not_found_in_trash' => '垃圾桶中沒有目的地'
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail', 'excerpt'),
        'menu_icon' => 'dashicons-location-alt',
        'show_in_rest' => true
    ));

    // 客戶見證文章類型
    register_post_type('testimonial', array(
        'labels' => array(
            'name' => '客戶見證',
            'singular_name' => '見證',
            'add_new' => '新增見證',
            'add_new_item' => '新增客戶見證',
            'edit_item' => '編輯見證',
            'new_item' => '新見證',
            'view_item' => '查看見證',
            'search_items' => '搜尋見證',
            'not_found' => '找不到見證',
            'not_found_in_trash' => '垃圾桶中沒有見證'
        ),
        'public' => true,
        'supports' => array('title', 'editor', 'thumbnail'),
        'menu_icon' => 'dashicons-testimonial',
        'show_in_rest' => true
    ));

    // 旅遊套裝行程
    register_post_type('tour_package', array(
        'labels' => array(
            'name' => '套裝行程',
            'singular_name' => '行程',
            'add_new' => '新增行程',
            'add_new_item' => '新增套裝行程',
            'edit_item' => '編輯行程',
            'new_item' => '新行程',
            'view_item' => '查看行程',
            'search_items' => '搜尋行程',
            'not_found' => '找不到行程',
            'not_found_in_trash' => '垃圾桶中沒有行程'
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail', 'excerpt'),
        'menu_icon' => 'dashicons-calendar-alt',
        'show_in_rest' => true
    ));
}
add_action('init', 'naturetour_custom_post_types');

/**
 * ==========================================================================
 * 自訂分類法
 * ==========================================================================
 */

function naturetour_custom_taxonomies() {
    // 目的地分類
    register_taxonomy('destination_category', 'destination', array(
        'labels' => array(
            'name' => '目的地分類',
            'singular_name' => '分類',
            'search_items' => '搜尋分類',
            'all_items' => '所有分類',
            'parent_item' => '上層分類',
            'parent_item_colon' => '上層分類:',
            'edit_item' => '編輯分類',
            'update_item' => '更新分類',
            'add_new_item' => '新增分類',
            'new_item_name' => '新分類名稱',
            'menu_name' => '目的地分類'
        ),
        'hierarchical' => true,
        'show_ui' => true,
        'show_admin_column' => true,
        'query_var' => true,
        'rewrite' => array('slug' => 'destination-category')
    ));

    // 行程標籤
    register_taxonomy('tour_tag', 'tour_package', array(
        'labels' => array(
            'name' => '行程標籤',
            'singular_name' => '標籤',
            'search_items' => '搜尋標籤',
            'popular_items' => '熱門標籤',
            'all_items' => '所有標籤',
            'edit_item' => '編輯標籤',
            'update_item' => '更新標籤',
            'add_new_item' => '新增標籤',
            'new_item_name' => '新標籤名稱',
            'menu_name' => '行程標籤'
        ),
        'hierarchical' => false,
        'show_ui' => true,
        'show_admin_column' => true,
        'query_var' => true,
        'rewrite' => array('slug' => 'tour-tag')
    ));
}
add_action('init', 'naturetour_custom_taxonomies');

/**
 * ==========================================================================
 * 自訂欄位支援
 * ==========================================================================
 */

function naturetour_custom_fields() {
    // 目的地自訂欄位
    add_action('add_meta_boxes', function() {
        add_meta_box(
            'destination_details',
            '目的地詳細資訊',
            'naturetour_destination_meta_box',
            'destination',
            'normal',
            'high'
        );
    });

    // 套裝行程自訂欄位
    add_action('add_meta_boxes', function() {
        add_meta_box(
            'tour_package_details',
            '行程詳細資訊',
            'naturetour_tour_package_meta_box',
            'tour_package',
            'normal',
            'high'
        );
    });
}
add_action('init', 'naturetour_custom_fields');

// 目的地詳細資訊meta box
function naturetour_destination_meta_box($post) {
    wp_nonce_field('naturetour_destination_meta', 'naturetour_destination_nonce');

    $best_time = get_post_meta($post->ID, '_destination_best_time', true);
    $visa_required = get_post_meta($post->ID, '_destination_visa_required', true);
    $currency = get_post_meta($post->ID, '_destination_currency', true);
    $language = get_post_meta($post->ID, '_destination_language', true);
    $timezone = get_post_meta($post->ID, '_destination_timezone', true);

    echo '<table class="form-table">';
    echo '<tr><th><label>最佳旅遊時間</label></th><td><input type="text" name="destination_best_time" value="' . esc_attr($best_time) . '" class="regular-text" /></td></tr>';
    echo '<tr><th><label>簽證需求</label></th><td><select name="destination_visa_required"><option value="yes"' . selected($visa_required, 'yes', false) . '>需要</option><option value="no"' . selected($visa_required, 'no', false) . '>不需要</option></select></td></tr>';
    echo '<tr><th><label>貨幣</label></th><td><input type="text" name="destination_currency" value="' . esc_attr($currency) . '" class="regular-text" /></td></tr>';
    echo '<tr><th><label>語言</label></th><td><input type="text" name="destination_language" value="' . esc_attr($language) . '" class="regular-text" /></td></tr>';
    echo '<tr><th><label>時區</label></th><td><input type="text" name="destination_timezone" value="' . esc_attr($timezone) . '" class="regular-text" /></td></tr>';
    echo '</table>';
}

// 套裝行程詳細資訊meta box
function naturetour_tour_package_meta_box($post) {
    wp_nonce_field('naturetour_tour_package_meta', 'naturetour_tour_package_nonce');

    $duration = get_post_meta($post->ID, '_tour_duration', true);
    $price = get_post_meta($post->ID, '_tour_price', true);
    $max_people = get_post_meta($post->ID, '_tour_max_people', true);
    $difficulty = get_post_meta($post->ID, '_tour_difficulty', true);
    $includes = get_post_meta($post->ID, '_tour_includes', true);

    echo '<table class="form-table">';
    echo '<tr><th><label>行程天數</label></th><td><input type="number" name="tour_duration" value="' . esc_attr($duration) . '" min="1" /> 天</td></tr>';
    echo '<tr><th><label>價格</label></th><td><input type="number" name="tour_price" value="' . esc_attr($price) . '" min="0" step="100" /> 元起</td></tr>';
    echo '<tr><th><label>最多人數</label></th><td><input type="number" name="tour_max_people" value="' . esc_attr($max_people) . '" min="1" /> 人</td></tr>';
    echo '<tr><th><label>難度等級</label></th><td><select name="tour_difficulty">';
    echo '<option value="easy"' . selected($difficulty, 'easy', false) . '>輕鬆</option>';
    echo '<option value="moderate"' . selected($difficulty, 'moderate', false) . '>中等</option>';
    echo '<option value="challenging"' . selected($difficulty, 'challenging', false) . '>挑戰</option>';
    echo '</select></td></tr>';
    echo '<tr><th><label>行程包含</label></th><td><textarea name="tour_includes" rows="4" class="large-text">' . esc_textarea($includes) . '</textarea></td></tr>';
    echo '</table>';
}

// 儲存自訂欄位
add_action('save_post', function($post_id) {
    // 目的地欄位儲存
    if (isset($_POST['naturetour_destination_nonce']) && wp_verify_nonce($_POST['naturetour_destination_nonce'], 'naturetour_destination_meta')) {
        update_post_meta($post_id, '_destination_best_time', sanitize_text_field($_POST['destination_best_time']));
        update_post_meta($post_id, '_destination_visa_required', sanitize_text_field($_POST['destination_visa_required']));
        update_post_meta($post_id, '_destination_currency', sanitize_text_field($_POST['destination_currency']));
        update_post_meta($post_id, '_destination_language', sanitize_text_field($_POST['destination_language']));
        update_post_meta($post_id, '_destination_timezone', sanitize_text_field($_POST['destination_timezone']));
    }

    // 套裝行程欄位儲存
    if (isset($_POST['naturetour_tour_package_nonce']) && wp_verify_nonce($_POST['naturetour_tour_package_nonce'], 'naturetour_tour_package_meta')) {
        update_post_meta($post_id, '_tour_duration', absint($_POST['tour_duration']));
        update_post_meta($post_id, '_tour_price', absint($_POST['tour_price']));
        update_post_meta($post_id, '_tour_max_people', absint($_POST['tour_max_people']));
        update_post_meta($post_id, '_tour_difficulty', sanitize_text_field($_POST['tour_difficulty']));
        update_post_meta($post_id, '_tour_includes', sanitize_textarea_field($_POST['tour_includes']));
    }
});

/**
 * ==========================================================================
 * Elementor 支援
 * ==========================================================================
 */

// 載入自訂 Elementor 小工具
function naturetour_elementor_widgets() {
    if (did_action('elementor/loaded')) {
        require_once NATURETOUR_THEME_DIR . '/elementor-widgets/widgets-loader.php';
    }
}
add_action('init', 'naturetour_elementor_widgets');

/**
 * ==========================================================================
 * 管理員自訂功能
 * ==========================================================================
 */

// 自訂管理員樣式
function naturetour_admin_styles() {
    wp_enqueue_style('naturetour-admin', NATURETOUR_THEME_URI . '/assets/css/admin.css', array(), NATURETOUR_VERSION);
}
add_action('admin_enqueue_scripts', 'naturetour_admin_styles');

// 自訂登入頁面樣式
function naturetour_login_styles() {
    wp_enqueue_style('naturetour-login', NATURETOUR_THEME_URI . '/assets/css/login.css', array(), NATURETOUR_VERSION);
}
add_action('login_enqueue_scripts', 'naturetour_login_styles');

/**
 * ==========================================================================
 * 輔助函數
 * ==========================================================================
 */

// 取得目的地詳細資訊
function get_destination_info($post_id = null) {
    if (!$post_id) {
        global $post;
        $post_id = $post->ID;
    }

    return array(
        'best_time' => get_post_meta($post_id, '_destination_best_time', true),
        'visa_required' => get_post_meta($post_id, '_destination_visa_required', true),
        'currency' => get_post_meta($post_id, '_destination_currency', true),
        'language' => get_post_meta($post_id, '_destination_language', true),
        'timezone' => get_post_meta($post_id, '_destination_timezone', true)
    );
}

// 取得套裝行程詳細資訊
function get_tour_package_info($post_id = null) {
    if (!$post_id) {
        global $post;
        $post_id = $post->ID;
    }

    return array(
        'duration' => get_post_meta($post_id, '_tour_duration', true),
        'price' => get_post_meta($post_id, '_tour_price', true),
        'max_people' => get_post_meta($post_id, '_tour_max_people', true),
        'difficulty' => get_post_meta($post_id, '_tour_difficulty', true),
        'includes' => get_post_meta($post_id, '_tour_includes', true)
    );
}

// 格式化價格顯示
function format_tour_price($price) {
    return number_format($price) . ' 元起';
}

// 取得難度等級標籤
function get_difficulty_label($difficulty) {
    $labels = array(
        'easy' => '輕鬆',
        'moderate' => '中等',
        'challenging' => '挑戰'
    );

    return isset($labels[$difficulty]) ? $labels[$difficulty] : '未設定';
}

/**
 * ==========================================================================
 * 安全性與效能優化
 * ==========================================================================
 */

// 移除WordPress版本號
remove_action('wp_head', 'wp_generator');

// 禁用XML-RPC
add_filter('xmlrpc_enabled', '__return_false');

// 移除不必要的header
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'rsd_link');

// 清理wp_head
function naturetour_cleanup_head() {
    remove_action('wp_head', 'wp_generator');
    remove_action('wp_head', 'wp_shortlink_wp_head');
    remove_action('wp_head', 'adjacent_posts_rel_link_wp_head', 10);
}
add_action('init', 'naturetour_cleanup_head');

?>