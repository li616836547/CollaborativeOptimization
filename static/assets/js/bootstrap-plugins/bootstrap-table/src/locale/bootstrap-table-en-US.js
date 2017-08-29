/**
 * Bootstrap Table English translation
 * Author: Zhixin Wen<wenzhixin2010@gmail.com>
 */
define('bootstrap-plugins/bootstrap-table/src/locale/bootstrap-table-en-US',['$'],function(a){
    var jQuery = a("$");
    (function ($) {
        'use strict';

        $.fn.bootstrapTable.locales['en_US'] = {
            formatLoadingMessage: function () {
                return 'Loading, please wait...';
            },
            formatRecordsPerPage: function (pageNumber) {
                return pageNumber + ' records per page';
            },
            formatShowingRows: function (pageFrom, pageTo, totalRows) {
                return 'Showing ' + pageFrom + ' to ' + pageTo + ' of ' + totalRows + ' rows';
            },
            formatSearch: function () {
                return 'Search';
            },
            formatNoMatches: function () {
                return 'No matching records found';
            },
            formatPaginationSwitch: function () {
                return 'Hide/Show pagination';
            },
            formatRefresh: function () {
                return 'Refresh';
            },
            formatToggle: function () {
                return 'Toggle';
            },
            formatColumns: function () {
                return 'Columns';
            },
            formatAllRows: function () {
                return 'All';
            }
        };

        $.extend($.fn.bootstrapTable.defaults, $.fn.bootstrapTable.locales['en_US']);

    })(jQuery);
})