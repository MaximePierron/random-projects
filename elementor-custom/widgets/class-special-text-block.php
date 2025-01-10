<?php
/**
 * SpecialTextBlock class.
 *
 * @category   Class
 * @package    ElementorCustom
 * @subpackage WordPress
 * @author     Maxime Pierron <maxime@pierron.com>
 * @copyright  2023 Maxime Pierron
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://example.com/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 8.2.3
 */
namespace ElementorCustom\Widgets;

use ElementorPro\Base\Base_Widget;
use Elementor\Controls_Manager;
// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();
/**
 * SpecialTextBlock widget class.
 *
 * @since 1.0.0
 */
class SpecialTextBlock extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'specialtextblock', plugins_url( '/assets/css/specialtextblock.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'specialtextblock', plugins_url( '/assets/js/specialtextblock.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
	}
	/**
	 * Retrieve the widget name.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'special-text-block';
	}
	/**
	 * Retrieve the widget title.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return __( 'Special Text Block', 'elementor-custom' );
	}
	/**
	 * Retrieve the widget icon.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return ' eicon-t-letter-bold';
	}
	/**
	 * Retrieve the list of categories the widget belongs to.
	 *
	 * Used to determine where to display the widget in the editor.
	 *
	 * Note that currently Elementor supports only one category.
	 * When multiple categories passed, Elementor uses the first one.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return array( 'elementor-custom-widgets' );
	}
	
	/**
	 * Enqueue styles.
	 */
	public function get_style_depends() {
		return array( 'specialtextblock' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'specialtextblock' );
		}
		
	}

    /**
	 * Register the widget controls.
	 *
	 * Adds different input fields to allow the user to change and customize the widget settings.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _register_controls() {

		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Content', 'elementor-custom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

        $repeater = new \Elementor\Repeater();

		$repeater->add_control(
			'word_1',
			[
				'label' => esc_html__( 'Add a word', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'Word 1' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $repeater->add_control(
            'fancy_1',
            [
                'label' => esc_html__( 'Fancy', 'textdomain' ),
                'type' => \Elementor\Controls_Manager::SWITCHER,
            ]
        );

        $repeater->add_control(
			'word_1_link',
			[
				'label' => esc_html__( 'Add url', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::URL,
                'placeholder' => esc_html__( 'https://your-link.com', 'elementor-custom' ),
				'options' => [ 'url', 'is_external', 'nofollow' ],
				'default' => [
					'url' => '',
					'is_external' => true,
					'nofollow' => true,
				],
				'label_block' => true,
                'condition' => [
                    'fancy_1' => 'yes',
                ],
			]
		);

        $repeater->add_control(
			'word_2',
			[
				'label' => esc_html__( 'Add another word', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'Word 2' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $repeater->add_control(
            'fancy_2',
            [
                'label' => esc_html__( 'Fancy', 'textdomain' ),
                'type' => \Elementor\Controls_Manager::SWITCHER,
            ]
        );

        $repeater->add_control(
			'word_2_link',
			[
				'label' => esc_html__( 'Add url (not required)', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::URL,
                'placeholder' => esc_html__( 'https://your-link.com', 'elementor-custom' ),
				'options' => [ 'url', 'is_external', 'nofollow' ],
				'default' => [
					'url' => '',
					'is_external' => true,
					'nofollow' => true,
				],
				'label_block' => true,
                'condition' => [
                    'fancy_2' => 'yes',
                ],
			]
		);

        $this->add_control(
			'list',
			[
				'label' => esc_html__( 'Add lines', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => $repeater->get_controls(),
			]
		);

		$this->end_controls_section();
	}
	/**
	 * Render the widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function render() {
		$settings = $this->get_settings_for_display();
        ?>
        <div id="text">
        <?php
            if ( $settings['list'] ) {
                foreach (  $settings['list'] as $item ) {
                    echo '<div class="line">';
                    if ( 'yes' === $item['fancy_1'] ) {
                        if ( $item['word_1_link'] ) {
                            echo '<a href="' . $item['word_1_link']['url'] . '" target="_blank" class="word fancy fancy-link">' . $item['word_1'] . '</a>';
                        } else {
                            echo '<p class="word fancy fancy-link">' . $item['word_1'] . '</p>';
                        }
                    } else {
                        echo '<p class="word">' . $item['word_1'] . '</p>';
                    }
                    if ( 'yes' === $item['fancy_2'] ) {
                        if ( $item['word_2_link'] ) {
                            echo '<a href="' . $item['word_2_link']['url'] . '" target="_blank" class="word fancy fancy-link">' . $item['word_2'] . '</a>';
                        } else {
                            echo '<p class="word fancy fancy-link">' . $item['word_2'] . '</p>';
                        }
                    } else {
                        echo '<p class="word">' . $item['word_2'] . '</p>';
                    }
                    echo '</div>';                
                }
            }
        ?>
        </div>
        <?php
	}

	protected function content_template() {
		?>
        <div id="text">
            <# if ( settings.list.length ) { #>
                <# _.each( settings.list, function( item ) { #>
                    <div class="line">
                        <# if ( 'yes' === settings.fancy_1 ) { #>
                            <# if ( settings.word_1_link ) { #>
                                <a id="fancy-link" href="{{settings.word_1_link}}" target="_blank" class="word fancy">{{{ settings.word_1 }}}</a>
                            <# } else { #>
                                <p class="word fancy">{{{ settings.word_1 }}}</p>
                            <# } #>
                        <# } else { #>
                            <p class="word">{{{ settings.word_1 }}}</p>
                        <# } #>
                        <# if ( 'yes' === settings.fancy_2 ) { #>
                            <# if ( settings.word_2_link ) { #>
                                <a href="{{settings.word_1_link}}" target="_blank" class="word fancy fancy-link">{{{ settings.word_2 }}}</a>
                            <# } else { #>
                                <p class="word fancy">{{{ settings.word_2 }}}</p>
                            <# } #>
                        <# } else { #>
                            <p class="word">{{{ settings.word_2 }}}</p>
                        <# } #>
                    </div>
                <# }); #>
            <# } #>
        </div>
		<?php
	}
}